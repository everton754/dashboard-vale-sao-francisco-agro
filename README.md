# 🍇 Vale do São Francisco Agro Dashboard

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3110/">
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+" />
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-1.51-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  </a>
  <a href="https://plotly.com/python/">
    <img src="https://img.shields.io/badge/Plotly-6.4-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge" alt="MIT License" />
  </a>
  <a href="https://github.com/everton754/dashboard-vale-sao-francisco-agro">
    <img src="https://img.shields.io/github/last-commit/everton754/dashboard-vale-sao-francisco-agro?style=for-the-badge" alt="Last Commit" />
  </a>
  <a href="https://github.com/everton754/dashboard-vale-sao-francisco-agro/stargazers">
    <img src="https://img.shields.io/github/stars/everton754/dashboard-vale-sao-francisco-agro?style=for-the-badge" alt="GitHub Stars" />
  </a>
</p>

![Dashboard preview](assets/demo_dashboard.gif)

---

## 🇧🇷 Português

### 📌 Visão Geral
Este projeto entrega um dashboard analítico interativo para acompanhar a fruticultura no Vale do São Francisco, com foco em **Uva** e **Manga** nos municípios de **Petrolina (PE)** e **Juazeiro (BA)**.

A aplicação integra e trata dados de produção agrícola e preços médios para facilitar análises de:
- evolução temporal;
- participação por município;
- desempenho produtivo;
- variação de valor econômico da produção.

### 🎯 Objetivos do Dashboard
- Consolidar, em uma interface única, os principais indicadores da fruticultura regional.
- Apoiar decisões estratégicas com filtros por município, produto e intervalo de anos.
- Transformar dados públicos em visualizações claras e acionáveis.

### ✨ Funcionalidades
- **KPIs principais** com comparação anual (produção e valor).
- **Séries temporais** para produção e valor econômico.
- **Análise geográfica** por participação de município.
- **Rendimento médio por produto** com comparativo visual.
- **Tabela detalhada interativa** com métricas consolidadas.
- **Filtros dinâmicos** no sidebar (município, produto e período).

### 🧱 Stack Tecnológica
- **App:** Streamlit
- **Manipulação de dados:** Pandas + NumPy
- **Visualização:** Plotly (Express + Graph Objects)
- **Linguagem:** Python 3.11+

### 📂 Estrutura do Projeto

```text
.
├── app.py                  # Aplicação principal Streamlit
├── assets/                 # GIFs, imagens e recursos visuais
├── data/
│   ├── raw/                # Dados brutos
│   └── processed/          # Dataset tratado usado no dashboard
├── notebooks/              # Exploração, limpeza e EDA
├── models/                 # Artefatos/modelos auxiliares
├── src/                    # Scripts e módulos de apoio
├── requirements.txt        # Dependências Python
└── LICENSE                 # Licença MIT
```

### ▶️ Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/everton754/dashboard-vale-sao-francisco-agro.git
cd dashboard-vale-sao-francisco-agro
```

2. (Opcional, recomendado) crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o dashboard:

```bash
streamlit run app.py
```

5. Acesse no navegador:

```text
http://localhost:8501
```

### ☁️ Deploy (Streamlit Community Cloud)
1. Faça push do projeto para seu GitHub.
2. Acesse `https://share.streamlit.io`.
3. Crie um novo app e configure:
   - **Repository:** `everton754/dashboard-vale-sao-francisco-agro`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Clique em **Deploy**.

### 🗃️ Fontes de Dados
- **IBGE / SIDRA (PAM):** Produção agrícola municipal.
- **CEPEA/ESALQ:** Referências de preços agropecuários.

> Observação: os dados processados já estão versionados no projeto para facilitar execução e demonstração.

### 👤 Autor
Desenvolvido por **Everton Santos**  
[LinkedIn](https://www.linkedin.com/in/everton-sant0s/)

---

## 🇺🇸 English

### 📌 Overview
This project delivers an interactive analytics dashboard for fruit farming in the São Francisco Valley, focused on **Grapes** and **Mangoes** in **Petrolina (PE)** and **Juazeiro (BA)**.

The app integrates and cleans production and average-price data to support analysis of:
- time evolution;
- municipal share;
- productivity performance;
- production economic value changes.

### 🎯 Dashboard Goals
- Centralize key regional fruit-farming indicators in one interface.
- Support strategic decision-making with filters by city, product, and year range.
- Turn public datasets into clear, actionable visual insights.

### ✨ Features
- **Top KPIs** with year-over-year comparison (production and value).
- **Time-series charts** for production and economic value.
- **Geographic split** by municipal participation.
- **Average yield by product** with visual comparison.
- **Interactive detailed table** with consolidated metrics.
- **Dynamic sidebar filters** (city, product, and time range).

### 🧱 Tech Stack
- **App:** Streamlit
- **Data processing:** Pandas + NumPy
- **Visualization:** Plotly (Express + Graph Objects)
- **Language:** Python 3.11+

### 📂 Project Structure

```text
.
├── app.py                  # Main Streamlit application
├── assets/                 # GIFs, images, visual assets
├── data/
│   ├── raw/                # Raw source data
│   └── processed/          # Cleaned dataset used by the dashboard
├── notebooks/              # Exploration, cleaning, and EDA
├── models/                 # Supporting model/artifact files
├── src/                    # Helper scripts and modules
├── requirements.txt        # Python dependencies
└── LICENSE                 # MIT license
```

### ▶️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/everton754/dashboard-vale-sao-francisco-agro.git
cd dashboard-vale-sao-francisco-agro
```

2. (Optional, recommended) create and activate a virtual environment:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the dashboard:

```bash
streamlit run app.py
```

5. Open in your browser:

```text
http://localhost:8501
```

### ☁️ Deployment (Streamlit Community Cloud)
1. Push the project to your GitHub account.
2. Go to `https://share.streamlit.io`.
3. Create a new app and set:
   - **Repository:** `everton754/dashboard-vale-sao-francisco-agro`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy**.

### 🗃️ Data Sources
- **IBGE / SIDRA (PAM):** Municipal agricultural production.
- **CEPEA/ESALQ:** Agricultural price references.

> Note: processed data is versioned in this repository to simplify local execution and demos.

### 👤 Author
Built by **Everton Santos**  
[LinkedIn](https://www.linkedin.com/in/everton-sant0s/)
