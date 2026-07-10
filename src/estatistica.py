# Criar funções estatísticas para análise de dados
def media(dados):
    if not dados:
        return 0
    return sum(dados) / len(dados)

def variancia(dados):
    m = media(dados)
    if not dados:
        return 0
    return sum((x - m) ** 2 for x in dados) / len(dados)

def desvio_padrao(dados):
    if not dados:
        return 0    
    return variancia(dados) ** 0.5
