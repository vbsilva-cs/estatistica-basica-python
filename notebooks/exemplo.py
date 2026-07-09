# importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Adiciona o caminho do diretório src ao sys.path para importar o módulo estatistica
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# módulo estatistica.py deve estar localizado no diretório src
from estatistica import media, variancia, desvio_padrao

def main():
    # Dataset fictício
    dados = pd.DataFrame({"Notas": [7.5, 8.0, 6.5, 9.0, 7.0]})

    # Calcula e imprime a média, variância e desvio padrão das notas
    print("Média:", media(dados["Notas"]))
    print("Variância:", variancia(dados["Notas"]))
    print("Desvio Padrão:", desvio_padrao(dados["Notas"]))


if __name__ == "__main__":
    main()