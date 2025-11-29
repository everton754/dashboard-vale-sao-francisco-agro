from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
page_title="Vale do São Francisco - Dashboard Analítico",
page_icon="🍇",
layout="wide",
initial_sidebar_state="expanded"
)

CORES = {
'uva': '#6A1B9A',
'manga': '#FFA000',
'petrolina': '#2E7D32',
'juazeiro': '#1976D2'
}

@st.cache_data
def load_data():
    # Constrói o caminho absoluto para o arquivo, tornando o script mais robusto
    script_dir = Path(__file__).parent
    csv_path = script_dir / "data" / "processed" / "pam_censo_agro_integrado_v2.csv"

    if not csv_path.exists():
        st.error(f"❌ Arquivo não encontrado: {csv_path}")
        st.stop()

    df = pd.read_csv(csv_path)

    # =======================================================
    # CORREÇÃO CRÍTICA: Remover espaços antes da renomeação
    # =======================================================
    df.columns = df.columns.str.strip()

    # Renomeia colunas para um padrão consistente
    if 'preco_medio_r$_kg' in df.columns:
        df = df.rename(columns={'preco_medio_r$_kg': 'preco_medio_anual_r$_kg'})
    
    if 'quantidade_produzida_t' in df.columns:
        df = df.rename(columns={'quantidade_produzida_t': 'quantidade_produzida_ton'})

    # =======================================================
    # CORREÇÃO FINAL: CONVERSÃO DE TIPOS PARA EVITAR TYPEERROR
    # =======================================================
    colunas_numericas = [
        'quantidade_produzida_ton', 
        'preco_medio_anual_r$_kg', 
        'rendimento_medio_kg_ha',
        'area_colhida_ha' # Adicionando esta também, por segurança
    ]
    
    for col in colunas_numericas:
        if col in df.columns:
            # Garante que a coluna é numérica, transformando erros em NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # Remove linhas onde a quantidade ou preço ficou NaN após a coerção (limpeza de dados ruins)
    df.dropna(subset=['quantidade_produzida_ton', 'preco_medio_anual_r$_kg'], inplace=True)
    
    # Filtra preços zerados que podem distorcer as médias e os cálculos de valor
    df = df[df['preco_medio_anual_r$_kg'] > 0].copy() 

    df['ano'] = df['ano'].astype(int)

    return df

def formatar_numero(valor, prefixo="", sufixo="", decimais=0):
    if pd.isna(valor):
        return "N/A"

    formato = f"{{:,.{decimais}f}}"
    numero_formatado = formato.format(valor)
    return f"{prefixo}{numero_formatado}{sufixo}"

df = load_data()

df['valor_producao_milhoes'] = (
df['quantidade_produzida_ton'] * df['preco_medio_anual_r$_kg']
) / 1_000_000

st.sidebar.header("🔍 Filtros de Análise")

municipios_disponiveis = sorted(df['municipio'].unique())
municipios_selecionados = st.sidebar.multiselect(
"Município",
options=municipios_disponiveis,
default=municipios_disponiveis
)

produtos_disponiveis = sorted(df['produto'].unique())
produtos_selecionados = st.sidebar.multiselect(
"Produto",
options=produtos_disponiveis,
default=produtos_disponiveis
)

ano_min, ano_max = int(df['ano'].min()), int(df['ano'].max())
anos_selecionados = st.sidebar.slider(
"Período (anos)",
min_value=ano_min,
max_value=ano_max,
value=(ano_min, ano_max)
)

df_filtrado = df[
(df['municipio'].isin(municipios_selecionados)) &
(df['produto'].isin(produtos_selecionados)) &
# CORREÇÃO: Filtrar usando os valores min e max da tupla 'anos_selecionados'
(df['ano'] >= anos_selecionados[0]) &
(df['ano'] <= anos_selecionados[1])
]

if len(df_filtrado) == 0:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados. Ajuste os filtros na barra lateral.")
    st.stop()

st.title("🍇 Vale do São Francisco: Análise Estratégica da Fruticultura")

# CORREÇÃO: Exibir os anos min e max corretamente
st.markdown(f"""
Período: {anos_selecionados[0]} - {anos_selecionados[1]} | Fonte: IBGE (PAM) + CEPEA
Dashboard interativo de {', '.join(produtos_selecionados)} em {', '.join(municipios_selecionados)}
""")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

producao_total = df_filtrado['quantidade_produzida_ton'].sum()
with col1:
    st.metric(
label="📦 Produção Total",
value=formatar_numero(producao_total, sufixo=" ton")
)

valor_total = df_filtrado['valor_producao_milhoes'].sum()
with col2:
    st.metric(
label="💰 Valor de Produção",
value=formatar_numero(valor_total, prefixo="R$ ", sufixo=" Mi", decimais=1)
)

rendimento_medio = df_filtrado['rendimento_medio_kg_ha'].mean()
with col3:
    st.metric(
label="📈 Rendimento Médio",
value=formatar_numero(rendimento_medio, sufixo=" kg/ha")
)

preco_medio = df_filtrado['preco_medio_anual_r$_kg'].mean()
with col4:
    st.metric(
label="💵 Preço Médio",
value=formatar_numero(preco_medio, prefixo="R$ ", decimais=2)
)

st.markdown("---")

st.header("📊 Evolução Temporal")

df_temporal = df_filtrado.groupby(['ano', 'produto'], as_index=False).agg({
'quantidade_produzida_ton': 'sum',
'valor_producao_milhoes': 'sum'
})

tab1, tab2 = st.tabs(["📈 Produção (Toneladas)", "💰 Valor Econômico (R$)"])

with tab1:
    fig_producao = px.line(
df_temporal,
x='ano',
y='quantidade_produzida_ton',
color='produto',
markers=True,
title="Produção por Produto (Toneladas)",
labels={
'ano': 'Ano',
'quantidade_produzida_ton': 'Produção (ton)',
'produto': 'Produto'
},
color_discrete_map={'Uva': CORES['uva'], 'Manga': CORES['manga']}
)
fig_producao.update_layout(hovermode='x unified', height=400)
st.plotly_chart(fig_producao, use_container_width=True)

with tab2:
    fig_valor = px.area(
df_temporal,
x='ano',
y='valor_producao_milhoes',
color='produto',
title="Valor de Produção (R$ Milhões)",
labels={
'ano': 'Ano',
'valor_producao_milhoes': 'Valor (R$ Mi)',
'produto': 'Produto'
},
color_discrete_map={'Uva': CORES['uva'], 'Manga': CORES['manga']}
)
fig_valor.update_layout(hovermode='x unified', height=400)
st.plotly_chart(fig_valor, use_container_width=True)

st.markdown("---")

st.header("🗺️ Análise Geográfica e Produtividade")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Participação por Município")
df_municipal = df_filtrado.groupby('municipio', as_index=False).agg({
'quantidade_produzida_ton': 'sum'
})

fig_municipio = px.pie(
    df_municipal,
    names='municipio',
    values='quantidade_produzida_ton',
    title="Distribuição da Produção por Município",
    color_discrete_sequence=[CORES['petrolina'], CORES['juazeiro']]
)
fig_municipio.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_municipio, use_container_width=True)
with col2:
    st.subheader("Rendimento por Produto")
df_rendimento = df_filtrado.groupby('produto', as_index=False).agg({
'rendimento_medio_kg_ha': 'mean'
})

fig_rendimento = px.bar(
    df_rendimento,
    x='produto',
    y='rendimento_medio_kg_ha',
    title="Rendimento Médio por Produto (kg/ha)",
    color='produto',
    color_discrete_map={'Uva': CORES['uva'], 'Manga': CORES['manga']},
    text='rendimento_medio_kg_ha'
)
fig_rendimento.update_traces(
    texttemplate='%{text:,.0f}', 
    textposition='outside'
)
fig_rendimento.update_layout(showlegend=False)
st.plotly_chart(fig_rendimento, use_container_width=True)
st.markdown("---")
# ==================================================================
# TABELA INTERATIVA
# ==================================================================
st.header("📋 Dados Detalhados")

df_display = df_filtrado[[
    'municipio', 'ano', 'produto', 'area_colhida_ha',
    'quantidade_produzida_ton', 'rendimento_medio_kg_ha',
    'preco_medio_anual_r$_kg', 'valor_producao_milhoes'
]].copy()

df_display.columns = [
    'Município', 'Ano', 'Produto', 'Área (ha)',
    'Produção (ton)', 'Rendimento (kg/ha)', 'Preço (R$/kg)', 'Valor (R$ Mi)'
]

df_display['Área (ha)'] = df_display['Área (ha)'].apply(lambda x: f"{x:,.0f}")
df_display['Produção (ton)'] = df_display['Produção (ton)'].apply(lambda x: f"{x:,.0f}")
df_display['Rendimento (kg/ha)'] = df_display['Rendimento (kg/ha)'].apply(lambda x: f"{x:,.0f}")
df_display['Preço (R$/kg)'] = df_display['Preço (R$/kg)'].apply(lambda x: f"R$ {x:.2f}")
df_display['Valor (R$ Mi)'] = df_display['Valor (R$ Mi)'].apply(lambda x: f"R$ {x:.2f}")

st.dataframe(
    df_display.sort_values(
        ['Ano', 'Município', 'Produto'], 
        ascending=[False, True, True]
    ),
    use_container_width=True,
    hide_index=True
)

# ==================================================================
# DOWNLOAD DE DADOS
# ==================================================================
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar Dados Filtrados (CSV)",
    data=csv,
    file_name='vsf_dados_filtrados.csv',
    mime='text/csv',
)

st.markdown("---")

# ==================================================================
# INSIGHTS ESTRATÉGICOS
# ==================================================================
st.header("💡 Principais Insights")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **🚀 Crescimento da Uva**  
    A uva apresentou crescimento de **252%** em produção entre 2013-2024, 
    com CAGR de **12.1%** no valor de produção.
    """)

with col2:
    st.success("""
    **🥭 Potencial da Manga**  
    Manga tem oportunidade de **+20% no rendimento** através de 
    irrigação tecnificada, podendo gerar **R$ 300 Mi/ano** adicionais.
    """)

# ==================================================================
# RODAPÉ
# ==================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Desenvolvido por:</strong> Everton Santos de Oliveira</p>
    <p>
        <a href="https://linkedin.com/in/evert0n-sant0s" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/everton754" target="_blank">GitHub</a> | 
        <a href="https://medium.com/@eso.datalab" target="_blank">Medium</a>
    </p>
    <p style='font-size: 0.9em;'>
        <strong>Fonte de Dados:</strong> IBGE (PAM) + CEPEA<br>
        <strong>Última Atualização:</strong> Novembro 2025
    </p>
</div>
""", unsafe_allow_html=True)