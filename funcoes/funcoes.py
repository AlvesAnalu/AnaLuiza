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

def calcula_pontos_regra_simples(face_dos_dados):
    dic_pontos={}
    for i in range(1,7):
        dic_pontos[i]= 0
    for dado in face_dos_dados:
        dic_pontos[dado]+= dado
    return dic_pontos

def calcula_pontos_soma(face_dados):
    soma= 0
    for face in face_dados:
        soma+= face
    return soma