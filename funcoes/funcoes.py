import random

def rolar_dados(quantos_dados):
    resultados_dados= []
    for i in range(quantos_dados):
        resultados_dados.append(random.randint(1,6))
    return resultados_dados

def guardar_dado(dados_rolados, dados_guardados, indice):
    valor= dados_rolados[indice]
    novos_rolados= dados_rolados+[valor]
    novos_guardados= novos_guardados+[valor]
    dados_escolhidos= [novos_rolados, novos_guardados]
    return dados_escolhidos