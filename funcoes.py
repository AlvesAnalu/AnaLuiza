import random

def rolar_dados(quantos_dados):
    resultados_dados= []
    for i in range(quantos_dados):
        resultados_dados.append(random.randint(1,6))
    return resultados_dados