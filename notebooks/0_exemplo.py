import pandas as pd
import numpy as np
from src.estatistica import media, variancia, desvio_padrao

# Dataset fictício
dados = pd.DataFrame({"Notas": [7.5, 8.0, 6.5, 9.0, 7.0]})

print("Média:", media(dados["Notas"]))
print("Variância:", variancia(dados["Notas"]))
print("Desvio Padrão:", desvio_padrao(dados["Notas"]))