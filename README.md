# API Loterias - Versão Gratuita

Bem-vindo ao **API Loterias - Free Version**, a versão gratuita do site [apiloterias.com](https://apiloterias.com), que fornece resultados de loterias com filtros avançados.  

Esta versão **gratuita** é hospedada via **GitHub Pages** e fornece acesso limitado a alguns endpoints de consulta para cada loteria, permitindo que você acesse resultados de concursos de forma rápida e prática.  

---

## 🔹 Loterias Disponíveis na Versão Gratuita

A versão gratuita fornece resultados para **todos os jogos de loteria**, incluindo:

- Mega-Sena  
- Lotofácil  
- Lotomania  
- Federal  
- Timemania  
- Loteca  
- E outros que forem adicionados futuramente

---

## 🔹 Endpoints da Versão Gratuita

Na versão gratuita, você possui **consultas básicas** de concursos de cada loteria:

| Endpoint | Descrição | Exemplo |
|----------|-----------|---------|
| `/NOME-LOTERIA/concurso/NUMERO` | Retorna os detalhes de um concurso específico pelo número. | `/megasena/concurso/1` |
| `/NOME-LOTERIA/concurso/ultimo` | Retorna o concurso mais recente da loteria. | `/lotofacil/concurso/ultimo` |
| `/NOME-LOTERIA/concurso/todos` | Retorna todos os concursos disponíveis da loteria. | `/lotomania/concurso/todos` |

> Todos os concursos são retornados como arquivos JSON individuais ou completos, sem paginação.  

---

## 🔹 Projeto Pago (API Oficial)

O **projeto principal**, disponível em [apiloterias.com](https://apiloterias.com), oferece uma **API completa e sofisticada** para assinantes, com **endpoints avançados** para consultas detalhadas, estatísticas e análises históricas, incluindo:

- Concurso específico pelo número  
- Último concurso  
- Últimos X concursos  
- Paginação de todos os concursos  
- Números mais frequentes (quentes) e menos frequentes (frios)  
- Números mais atrasados  
- Sequências comuns  
- Distribuição de pares e ímpares  
- Distribuição do somatório das dezenas  
- Simulador de apostas contra histórico completo  

> A API paga permite consultas detalhadas para todas as loterias, com estatísticas avançadas, filtros por ano, frequências, atrasos, somatórios e simulações personalizadas.

---

## 🔹 Diferenças Entre Gratuito e Pago

| Recurso | Gratuito | Pago |
|---------|----------|------|
| Acesso a concursos | ✅ Todos os jogos | ✅ Todos os jogos |
| Último concurso | ✅ | ✅ |
| Concurso específico | ✅ | ✅ |
| Todos os concursos | ❌ | ✅ (com paginação) |
| Frequência de números | ❌ | ✅ (quentes, frios, atrasados) |
| Sequências comuns | ❌ | ✅ |
| Pares e ímpares | ❌ | ✅ |
| Soma das dezenas | ❌ | ✅ |
| Simulador de apostas | ❌ | ✅ |
| Filtros avançados | ❌ | ✅ |

---

## 🔹 Como Utilizar a Versão Gratuita

Você pode consumir os arquivos JSON diretamente via GitHub Pages. Exemplos:

```bash
# Último concurso da Mega-Sena
curl https://maickon.github.io/free-apiloterias/database/megasena/ultimo.json

# Concurso número 1 da Lotofácil
curl https://maickon.github.io/free-apiloterias/database/lotofacil/1.json

# Todos os concursos da Lotomania
curl https://maickon.github.io/free-apiloterias/database/lotomania/todos.json
