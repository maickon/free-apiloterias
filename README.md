# API Loterias - Versão Gratuita

Bem-vindo ao **API Loterias - Free Version**, a versão gratuita do site [apiloterias.com](https://apiloterias.com), que fornece resultados de loterias com filtros avançados.  

Esta versão **gratuita** é hospedada via **GitHub Pages** e fornece acesso limitado a alguns endpoints de consulta para cada loteria, permitindo que você acesse resultados de concursos de forma rápida e prática.  

---

## 🔹 Loterias Disponíveis na Versão Gratuita

Atualmente, a versão gratuita possui suporte para:

- **Mega-Sena**
- Futuramente podem ser adicionadas outras loterias com suporte similar (ex: Lotofácil, Lotomania, Federal, etc.)

---

## 🔹 Endpoints da Versão Gratuita

Na versão gratuita, você possui **apenas consultas básicas** de concursos da Mega-Sena:

| Endpoint | Descrição | Exemplo |
|----------|-----------|---------|
| `/megasena/concurso/1` | Retorna os detalhes do concurso de número 1. | `https://usuario.github.io/free-api/megasena/concurso/1.json` |
| `/megasena/concurso/todos` | Retorna todos os concursos disponíveis. | `https://usuario.github.io/free-api/megasena/concurso/todos.json` |
| `/megasena/concurso/ultimo` | Retorna o concurso mais recente. | `https://usuario.github.io/free-api/megasena/concurso/ultimo.json` |

> Cada concurso está disponível como um arquivo JSON independente, facilitando a leitura e integração com aplicações externas.

---

## 🔹 Projeto Pago (API Oficial)

O **projeto principal**, disponível em [apiloterias.com](https://apiloterias.com), oferece uma **API completa e sofisticada** para assinantes.  

Diferentemente da versão gratuita, a API paga possui **endpoints avançados** para consultas detalhadas, estatísticas e análises históricas:

| Endpoint | Descrição |
|----------|-----------|
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/NUMERO-DO-CONCURSO` | Retorna um concurso específico pelo seu número. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO` | Retorna o concurso mais recente. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/ultimosX` | Retorna os últimos X concursos. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/todos/paginaX` | Retorna todos os concursos com paginação (30 resultados por página). |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/frequencia/quente/X` | Retorna os X números que mais saíram (maior frequência). |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/frequencia/frio/X` | Retorna os X números que menos saíram (menor frequência). |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/frequencia/mais-atrasados/X` | Retorna os números mais atrasados (que não saem há mais tempo). |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/sequencias-comuns` | Retorna sequências de números que mais se repetiram nos concursos. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/pares-impares` | Retorna a distribuição de números pares e ímpares em todos os concursos. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/soma-dezenas/X` | Retorna a distribuição do somatório das dezenas nos últimos X concursos. |
| `/v1/NOME-LOTERIA/CHAVE-DE-ACESSO/simulador` | Simula uma aposta contra todo o histórico de resultados e retorna análise detalhada de desempenho. |

> A API paga permite consultas detalhadas para todas as loterias, com estatísticas avançadas, filtros por ano, frequências, atrasos, somatórios e simulações personalizadas.

---

## 🔹 Diferenças Entre Gratuito e Pago

| Recurso | Gratuito | Pago |
|---------|----------|------|
| Acesso a concursos | Apenas Mega-Sena | Todas as loterias |
| Último concurso | ✅ | ✅ |
| Concurso específico | ✅ | ✅ |
| Todos os concursos | ✅ | ✅ (com paginação avançada) |
| Frequência de números | ❌ | ✅ (quentes, frios, atrasados) |
| Sequências comuns | ❌ | ✅ |
| Pares e ímpares | ❌ | ✅ |
| Soma das dezenas | ❌ | ✅ |
| Simulador de apostas | ❌ | ✅ |
| Filtros avançados | ❌ | ✅ |

---

## 🔹 Como Utilizar a Versão Gratuita

Você pode consumir os arquivos JSON diretamente via GitHub Pages. Exemplo:

```bash
# Último concurso da Mega-Sena
curl https://usuario.github.io/free-api/megasena/concurso/ultimo.json

# Concurso número 1
curl https://usuario.github.io/free-api/megasena/concurso/1.json

# Todos os concursos
curl https://usuario.github.io/free-api/megasena/concurso/todos.json
