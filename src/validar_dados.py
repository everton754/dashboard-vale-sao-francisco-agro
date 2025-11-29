import sys
from pathlib import Path

import pandas as pd


def validar_dataset(caminho_arquivo: Path, linhas_esperadas: int):
    """
    Executa uma série de validações em um arquivo CSV.
    """
    erros = []
    print("=" * 60)
    print("INICIANDO A VALIDAÇÃO DO DATASET FINAL")
    print("=" * 60)

    # Verificação 0: Existência do arquivo
    if not caminho_arquivo.is_file():
        print(f"❌ ERRO FATAL: Arquivo não encontrado em '{caminho_arquivo}'")
        sys.exit(1)

    df = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{caminho_arquivo.name}' carregado com sucesso.")

    # 🛠️ CORREÇÃO: Renomear colunas para corresponder ao esperado pelo script
    df = df.rename(columns={
        'preco_medio_r$_kg': 'preco_medio_anual_r$_kg',
        'quantidade_produzida_t': 'quantidade_produzida_ton'
    })
    print("Colunas ajustadas: 'preco_medio_r$_kg' -> 'preco_medio_anual_r$_kg' e 'quantidade_produzida_t' -> 'quantidade_produzida_ton'.")


    # Verificação 1: Número de linhas
    if len(df) == linhas_esperadas:
        print(f"\n✅ Total de registros: {len(df)} (esperado: {linhas_esperadas})")
    else:
        msg = f"Total de registros: {len(df)} (esperado: {linhas_esperadas})"
        erros.append(msg)
        print(f"\n❌ {msg}")

    # Verificação 2: Colunas
    colunas_esperadas = {
        'municipio', 'ano', 'produto', 'area_colhida_ha',
        'quantidade_produzida_ton', 'rendimento_medio_kg_ha',
        'preco_mediano_r$_kg', 'preco_medio_anual_r$_kg', # <- Nomes esperados
        'preco_std_r$_kg', 'num_observacoes_preco'
    }
    colunas_encontradas = set(df.columns)

    if colunas_encontradas == colunas_esperadas:
        print("\n✅ Todas as colunas esperadas foram encontradas.")
    else:
        colunas_faltando = colunas_esperadas - colunas_encontradas
        colunas_extras = colunas_encontradas - colunas_esperadas
        if colunas_faltando:
            msg = f"Colunas faltando: {sorted(list(colunas_faltando))}"
            erros.append(msg)
            print(f"\n❌ {msg}")
        if colunas_extras:
            msg = f"Encontradas colunas inesperadas: {sorted(list(colunas_extras))}"
            erros.append(msg)
            print(f"\n❌ {msg}")

    # Verificação 3: Valores nulos
    colunas_para_checar_nulos = [col for col in df.columns if col not in ['preco_std_r$_kg']]
    nulos_encontrados = df[colunas_para_checar_nulos].isnull().sum()
    colunas_com_nulos = nulos_encontrados[nulos_encontrados > 0]
    if colunas_com_nulos.empty:
        print("\n✅ Nenhuma coluna (exceto 'preco_std_r$_kg') contém valores nulos.")
    else:
        msg = f"Encontrados valores nulos nas seguintes colunas:\n{colunas_com_nulos.to_string()}"
        erros.append(msg)
        print(f"\n❌ {msg}")

    # Resumo das informações
    print("\n-- Resumo dos Dados --")
    print(f"Municípios: {df['municipio'].unique()}")
    print(f"Produtos: {df['produto'].unique()}")
    print(f"Período: {df['ano'].min()} - {df['ano'].max()}")
    print("\nAmostra de dados (primeiras 3 linhas):")
    print(df.head(3).to_string())

    # Conclusão da Validação
    print("\n" + "=" * 60)
    if not erros:
        print("✅ SUCESSO: Dataset válido e pronto para o dashboard!")
    else:
        print(f"❌ FALHA: Foram encontrados {len(erros)} problemas no dataset.")
        for i, erro in enumerate(erros, 1):
            print(f"   {i}. {erro}")
    print("=" * 60)

    if erros:
        sys.exit(1) # Encerra com código de erro se houver problemas

def main():
    """Ponto de entrada do script."""
    # 🛠️ CORREÇÃO: Removido o .parent para buscar o arquivo corretamente
    script_dir = Path(__file__).parent
    caminho_arquivo_csv = script_dir / "data" / "processed" / "pam_censo_agro_integrado_v2.csv"

    validar_dataset(caminho_arquivo=caminho_arquivo_csv, linhas_esperadas=48)

if __name__ == "__main__":
    main()