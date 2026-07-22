import random

# importando o modulo de sorteio ou aleatoriedade.
# dentro dele há uma função chamadad "randint" que usaremos para o sorteio da jogada da máquina.

# iniciando variaveis:

pontos_player = 0
pontos_cpu = 0
# jogadas
# 0 = pedra | 1 = papel | 2 = tesoura.
# números sao representantes mais leves do que palavras
jogada_player = 0
jogada_cpu = 0

# variavel auxiliar para controlar o loop
vai_sair = False

# loop while funciona em conjunto com uma condição. (tanto para entrar na primeira vez quanto para saber se vai repetir na proxima)
while vai_sair == False:

    print("BEM VINDO AO JO-KEN-PO!")
    print("-" * 10)
    print("0 - Pedra")
    print("1 - Papel")
    print("2 - Tesoura")
    print("Sua Jogada:")
    try:
        jogada_player = int(input("->"))
    except ValueError:
        print("Jogada Inexiatente!")
        input("Precione enter para continuar...")
        print("#" * 20)
        print("#" * 20)
        continue

    if jogada_player < 0 or jogada_player > 2:
        print("Jogada Inexiatente!")
        input("Precione enter para continuar...")
        print("#" * 20)
        print("#" * 20)
        continue

    # jogada da maquina. sorteia um numero inteiro (randint) entre 0 e 2
    jogada_cpu = random.randint(0, 2)
    # variaveis com o nome da jogada (para mostrar bonitinho pro jogador)
    nome_jogada_player = ""
    nome_jogada_cpu = ""

    match jogada_player:
        case 0:
            nome_jogada_player = "pedra"
        case 1:
            nome_jogada_player = "Papel"    
        case 2:
            nome_jogada_player = "Tesoura"    

    match jogada_cpu:
        case 0:
            nome_jogada_cpu = "Pedra"            
        case 1:
            nome_jogada_cpu = "Papel"    
        case 2:
            nome_jogada_cpu = "Tesoura"    

    print("A máquina jogou: ", nome_jogada_cpu)
    print("Você jogou", nome_jogada_player)
    # vitorias do player
    if jogada_player == 0 and jogada_cpu == 2:
        # player pedra e maquina tesoura = vitoria        
        print("Você venceu!")
        pontos_player = pontos_player + 1
    elif jogada_player == 1 and jogada_cpu == 0:
        # player papel e maquina pedra = vitoria
        print("Você venceu!!")
        pontos_player = pontos_player +1
    elif jogada_player == 2 and jogada_cpu == 1:
        # player tesoura e maquina papel = vitoria
        print("Você venceu!!")
        pontos_player = pontos_player +1
    elif jogada_player == 0 and jogada_cpu == 1:
        # player pedra maquina papel = derrota
        print("Você perdeu!!")
        pontos_cpu = pontos_cpu +1
    elif jogada_player == 1 and jogada_cpu == 2:
        # player papel maquina tesoura = derrota
        print("Você perdeu!!")
        pontos_cpu = pontos_cpu +1
    elif jogada_player == 2 and jogada_cpu == 0:
        # player tesoura maquina pedra = derrota
        print("Você perdeu!!")
        pontos_cpu = pontos_cpu +1
    else:
        # empate
        print("Empate!!")
    
    print(f"Placar - Você: {pontos_player} | Máquina: {pontos_cpu}")
    input("Precione enter para continuar...")
    print("#" * 20)
    print("#" * 20)