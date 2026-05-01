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

def calcula_pontos_sequencia_baixa(face_dados2):
    if 1 in face_dados2 and 2 in face_dados2 and 3 in face_dados2 and 4 in face_dados2:
        return 15
    if 2 in face_dados2 and 3 in face_dados2 and 4 in face_dados2 and 5 in face_dados2:
        return 15
    if 3 in face_dados2 and 4 in face_dados2 and 5 in face_dados2 and 6 in face_dados2:
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta(face_dados3):
    if 1 in face_dados3 and 2 in face_dados3 and 3 in face_dados3 and 4 in face_dados3 and 5 in face_dados3:
        return 30
    if 2 in face_dados3 and 3 in face_dados3 and 4 in face_dados3 and 5 in face_dados3 and 6 in face_dados3:
        return 30
    else:
        return 0

def calcula_pontos_full_house(face_dados4):
    faces_iguais= {}
    soma= 0
    for face in face_dados4:
        if face in faces_iguais:
            faces_iguais[face]+= 1
        else:
            faces_iguais[face]= 1
    if len(faces_iguais)!= 2:
        return 0
    valores= list(faces_iguais.values())
    if (valores[0]==3 and valores[1]==2) or (valores[0]==2 and valores[1]==3):
        for face in face_dados4:
            soma += face
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(face_dados5):
    contagem = {}
    for valor in face_dados5:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
    for valor in contagem:
        if contagem[valor] == 4:
            soma = 0
            for x in face_dados5:
                soma += x
            return soma
    return 0