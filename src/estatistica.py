# Criar funções estatísticas para análise de dados
def media(dados):
    return sum(dados) / len(dados)

def variancia(dados):
    m = media(dados)
    return sum((x - m) ** 2 for x in dados) / len(dados)

def desvio_padrao(dados):
    return variancia(dados) ** 0.5