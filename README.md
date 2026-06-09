# Automações em Python para Escritório e T.I. 🤖

"Este repositório contém scripts de automação de escritório desenvolvidos em Python. O objetivo é demonstrar a manipulação de arquivos CSV para tratamento de dados financeiros e modificação de arquivos de configuração JSON, simulando cenários reais de infraestrutura de TI."

## 🛠️ Tecnologias e Conceitos Utilizados
- **Python 3**
- **Biblioteca `csv`** (Nativa do Python para leitura de tabelas)
- **Biblioteca `json`** (Nativa do Python para manipulação de arquivos de configuração)
- **Manipulação de Strings e Tipos** (Uso de `.strip()` e conversão de dados para `float`)

## 📁 Detalhes dos Projetos

### 1. Consolidador de Relatórios (CSV)
- **Arquivo:** `analisador.py`
- **O que faz:** Lê um relatório bruto de funcionários em formato CSV, realiza a limpeza de dados (remoção de espaços em branco desnecessários), converte os salários de texto para número real e calcula o gasto total da folha de pagamento de forma automatizada.

### 2. Manipulador de Configurações (JSON)
- **Arquivo:** `analisador_json.py`
- **O que faz:** Simula a alteração de status de um servidor na nuvem AWS. O script lê um arquivo `config.json`, localiza a chave de configuração de status, altera seu valor para "ativo" em tempo real e grava a nova configuração de volta no disco.
