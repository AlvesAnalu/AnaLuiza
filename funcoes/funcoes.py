import random

def rolar_dados(quantos_dados):
    resultados_dados= []
    for i in range(quantos_dados):
        resultados_dados.append(random.randint(1,6))
    return resultados_dados

def guardar_dado(dados_rolados, dados_guardados, indice):
    valor = dados_rolados[indice]
    novos_rolados= dados_rolados[:indice]+dados_rolados[indice+1:]
    novos_guardados= dados_guardados+[valor]
    dados_escolhidos= [novos_rolados, novos_guardados]
    return dados_escolhidos

def remover_dado(rolados, guardados, indic):
    valor= guardados[indic]
    rolados_novos= rolados+[valor]
    guardados_novos= guardados[:indic]+guardados[indic+1:]
    novos_escolhidos= [rolados_novos, guardados_novos]
    return novos_escolhidos