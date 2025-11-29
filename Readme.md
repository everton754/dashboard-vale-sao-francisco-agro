# 🍇 Dashboard Analítico do Vale do São Francisco

![Demonstração do Dashboard](assets/demo_dashboard.gif)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-MVP%20Fase%201-green?style=for-the-badge)

## 🎯 Objetivo

Painel analítico desenvolvido para monitorar a produção e valor econômico da fruticultura (Uva e Manga) nos municípios de Petrolina-PE e Juazeiro-BA (2013-2024). O projeto integra dados do **IBGE (PAM)** e **CEPEA**, oferecendo insights estratégicos sobre produtividade e tendências de mercado.

## 📊 Funcionalidades

- **Evolução Temporal**: Séries históricas de produção (ton) e valor (R$).
- **Comparativo Regional**: Análise de market share entre Petrolina e Juazeiro.
- **Indicadores de Performance**: Métricas de rendimento médio (kg/ha) e preço médio.
- **Filtros Dinâmicos**: Segmentação por município, produto e período.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.11
- **ETL & Análise**: Pandas, NumPy
- **Visualização**: Plotly Express, Streamlit
- **Dados**: APIs públicas do IBGE (SIDRA) e CEPEA/Esalq

## Estrutura do Projeto

O pipeline de dados foi construído em etapas documentadas na pasta `notebooks/`:

1. **Ingestão**: Coleta automatizada de dados brutos.
2. **Limpeza**: Tratamento de outliers e padronização de esquemas.
3. **EDA**: Análise exploratória para validação de hipóteses.

## 🚀 Como Executar Localmente

1. Clone o repositório:

    ```bash
    git clone https://github.com/everton754/dashboard-vale-sao-francisco-agro.git
    ```

2. Navegue até o diretório do projeto e instale as dependências:

    ```bash
    cd dashboard-vale-sao-francisco-agro
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No Linux/Mac:
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Execute o dashboard:

    ```bash
    streamlit run app.py
    ```

## ☁️ Deploy no Streamlit Cloud

Para fazer o deploy da aplicação, siga estes passos:

1. Acesse share.streamlit.io.
2. Faça login com sua conta do GitHub.
3. Clique em **"New app"**.
4. Selecione o repositório `dashboard-vale-sao-francisco-agro`.
5. Configure com as seguintes opções:
    - **Branch**: `main`
    - **Main file path**: `app.py`
6. Clique em **"Deploy!"**.

## 👨‍💻 Autor

---
Desenvolvido por [Everton Santos](https://www.linkedin.com/in/everton-sant0s/)