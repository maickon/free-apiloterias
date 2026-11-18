#!/usr/bin/env python3
"""
Fetches new lottery results and updates database/{game}/ folders.

Required env var:
  LOTTERY_API_BASE  — base URL of the results API (set as a GitHub Secret)

Usage:
  python scripts/update.py              # all games
  python scripts/update.py megasena     # single game
"""
import json
import os
import ssl
import sys
import time
import urllib.request
from pathlib import Path

GAMES = [
    'diadesorte', 'duplasena', 'federal', 'loteca', 'lotofacil',
    'lotomania', 'maismilionaria', 'megasena', 'quina', 'supersete', 'timemania',
]

API_BASE  = os.environ.get('LOTTERY_API_BASE', '').rstrip('/')
DB_DIR    = Path(__file__).parent.parent / 'database'
HEADERS   = {
    'Accept':          'application/json',
    'User-Agent':      'Mozilla/5.0 (compatible; lottery-updater/2.0)',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

# Some govt endpoints have self-signed or chain-incomplete certs
_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode    = ssl.CERT_NONE


# ── helpers ──────────────────────────────────────────────────────────────────

def fetch(url: str, retries: int = 3) -> dict | None:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                if resp.status == 200:
                    return json.loads(resp.read().decode('utf-8'))
        except Exception as exc:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f'  [ERROR] {url} → {exc}')
    return None


def last_local_number(game_dir: Path) -> int:
    nums = [int(f.stem) for f in game_dir.glob('*.json') if f.stem.isdigit()]
    return max(nums) if nums else 0


def rebuild_todos(game_dir: Path) -> int:
    all_data = []
    files = sorted(
        (f for f in game_dir.glob('*.json') if f.stem.isdigit()),
        key=lambda f: int(f.stem),
    )
    for f in files:
        try:
            all_data.append(json.loads(f.read_text(encoding='utf-8')))
        except Exception:
            pass
    (game_dir / '_todos.json').write_text(
        json.dumps(all_data, ensure_ascii=False),
        encoding='utf-8',
    )
    return len(all_data)


# ── core ─────────────────────────────────────────────────────────────────────

def process_game(game: str) -> bool:
    """Returns True if at least one new concurso was saved."""
    game_dir = DB_DIR / game
    game_dir.mkdir(parents=True, exist_ok=True)

    last_local = last_local_number(game_dir)
    print(f'  local : {last_local or "none"}')

    latest = fetch(f'{API_BASE}/{game}')
    if not latest or 'numero' not in latest:
        print(f'  [SKIP] could not fetch latest for {game}')
        return False

    latest_num = int(latest['numero'])
    print(f'  remote: {latest_num}')

    if latest_num <= last_local:
        print(f'  up to date.')
        return False

    gap = latest_num - last_local
    print(f'  downloading {gap} new concurso(s)…')

    downloaded = 0
    for n in range(last_local + 1, latest_num + 1):
        data = latest if n == latest_num else fetch(f'{API_BASE}/{game}/{n}')
        if data is None:
            print(f'  [SKIP] concurso {n} — fetch failed')
            continue
        (game_dir / f'{n}.json').write_text(
            json.dumps(data, ensure_ascii=False), encoding='utf-8'
        )
        downloaded += 1
        if downloaded % 20 == 0 or n == latest_num:
            print(f'  [{downloaded}/{gap}] saved concurso {n}')
        time.sleep(0.15)   # polite delay between requests

    if downloaded > 0:
        count = rebuild_todos(game_dir)
        (game_dir / '_ultimo.json').write_text(
            json.dumps(latest, ensure_ascii=False), encoding='utf-8'
        )
        print(f'  _todos.json rebuilt ({count} total) · _ultimo.json updated.')

    return downloaded > 0


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    if not API_BASE:
        print('[FATAL] LOTTERY_API_BASE env var is not set.', file=sys.stderr)
        sys.exit(1)

    games   = sys.argv[1:] if len(sys.argv) > 1 else GAMES
    changed = []

    for game in games:
        print(f'\n── {game} ──')
        try:
            if process_game(game):
                changed.append(game)
        except Exception as exc:
            print(f'  [ERROR] {game}: {exc}')

    print(f'\n{"─" * 42}')
    if changed:
        print(f'Updated: {", ".join(changed)}')
    else:
        print('No new results found.')


if __name__ == '__main__':
    main()
