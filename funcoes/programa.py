from random import randint
import funcoes

def rolar_dados(qtd):
    dados = []
    i = 0
    while i < qtd:
        dados.append(randint(1, 6))
        i += 1
    return dados

cartela_de_pontos = {
    'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodada = 0
while rodada < 12:
    dados_guardados = []
    dados_rolados = rolar_dados(5)
    rerrolagens = 0
    jogada_finalizada = False
    while not jogada_finalizada:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if indice >= 0 and indice < len(dados_rolados):
                resultado = funcoes.guardar_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if indice >= 0 and indice < len(dados_guardados):
                resultado = funcoes.remover_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
        elif opcao == "3":
            if rerrolagens < 2:
                qtd = 5 - len(dados_guardados)
                dados_rolados = rolar_dados(qtd)
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")
        elif opcao == "4":
            funcoes.imprime_cartela(cartela_de_pontos)
        elif opcao == "0":
            print("Digite a combinação desejada:")
            categoria = input()
            todos_dados = dados_guardados + dados_rolados
            if categoria in ["1","2","3","4","5","6"]:
                cat_int = int(categoria)
                if cartela_de_pontos['regra_simples'][cat_int] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela_de_pontos = funcoes.faz_jogada(todos_dados, categoria, cartela_de_pontos)
                    jogada_finalizada = True
                    rodada += 1
            elif categoria in cartela_de_pontos['regra_avancada']:
                if cartela_de_pontos['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela_de_pontos = funcoes.faz_jogada(todos_dados, categoria, cartela_de_pontos)
                    jogada_finalizada = True
                    rodada += 1
            else:
                print("Combinação inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")
funcoes.imprime_cartela(cartela_de_pontos)
total = 0
for i in cartela_de_pontos['regra_simples']:
    if cartela_de_pontos['regra_simples'][i] != -1:
        total += cartela_de_pontos['regra_simples'][i]
soma_simples = 0
for i in cartela_de_pontos['regra_simples']:
    if cartela_de_pontos['regra_simples'][i] != -1:
        soma_simples += cartela_de_pontos['regra_simples'][i]
if soma_simples >= 63:
    total += 35
for i in cartela_de_pontos['regra_avancada']:
    if cartela_de_pontos['regra_avancada'][i] != -1:
        total += cartela_de_pontos['regra_avancada'][i]
print(f"Pontuação total: {total}")