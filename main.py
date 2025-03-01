import json
import xml.etree.ElementTree as ET
import pandas as pd

# 📌 QUESTÃO 1 - Cálculo da variável SOMA
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    print(f"Resultado da soma: {SOMA}")

# 📌 QUESTÃO 2 - Verifica se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def verificar_fibonacci():
    numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# 📌 QUESTÃO 3 - Processamento do faturamento diário
def carregar_dados_json(caminho):
    """Lê o arquivo JSON e retorna os dados."""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_dados_xml(caminho):
    """Lê o arquivo XML e retorna os dados."""
    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
    except ET.ParseError:
        print("Erro ao analisar o XML. Verifique a formatação do arquivo.")
        return []

    dados = []
    for row in root.findall("row"):
        try:
            dia = int(row.find("dia").text)
            valor = float(row.find("valor").text)
            dados.append({"dia": dia, "valor": valor})
        except (ValueError, AttributeError):
            print(f"Erro ao converter valores em um dos registros.")
    
    return dados

def analisar_faturamento(dados, fonte):
    """Processa os dados e calcula as estatísticas principais."""
    df = pd.DataFrame(dados)
    df_filtrado = df[df["valor"] > 0]

    if df_filtrado.empty:
        print(f"Nenhum dado de faturamento válido encontrado em {fonte}.")
        return

    menor_valor = df_filtrado["valor"].min()
    maior_valor = df_filtrado["valor"].max()
    media_mensal = df_filtrado["valor"].mean()
    dias_acima_media = (df_filtrado["valor"] > media_mensal).sum()

    print(f"\n🔹 Processando dados de faturamento ({fonte})...")
    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

# 📌 QUESTÃO 4 - Cálculo do percentual de faturamento por estado
def calcular_percentual_estados():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total_faturamento = sum(faturamento_estados.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}

    print("\nPercentual de faturamento por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# 📌 QUESTÃO 5 - Inversão de string sem usar funções prontas
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

def executar_inversao_string():
    entrada = input("Digite uma string para inverter: ")
    print(f"String invertida: {inverter_string(entrada)}")

# ---- EXECUÇÃO DO PROGRAMA ----
if __name__ == "__main__":
    print("\n🔹🔹 DESAFIO TARGET 🔹🔹\n")

    # 📌 QUESTÃO 1
    calcular_soma()

    # 📌 QUESTÃO 2
    verificar_fibonacci()

    # 📌 QUESTÃO 3
    caminho_json = "dados.json"
    caminho_xml = "dados.xml"
    
    print("\n🔹 Processando dados de faturamento (JSON)...")
    dados_json = carregar_dados_json(caminho_json)
    analisar_faturamento(dados_json, "JSON")

    print("\n🔹 Processando dados de faturamento (XML)...")
    dados_xml = carregar_dados_xml(caminho_xml)
    analisar_faturamento(dados_xml, "XML")

    # 📌 QUESTÃO 4
    calcular_percentual_estados()

    # 📌 QUESTÃO 5
    executar_inversao_string()
