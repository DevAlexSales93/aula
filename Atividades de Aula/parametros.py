def calcular_idade(ano_nascimento):
    print("Ano de Nascimento é:", ano_nascimento)
    idade = 2026 - ano_nascimento
    print("A idade é:", idade)
print("chamando a função")    
calcular_idade(1993)

meu_ano_nascimento = 1993
calcular_idade(meu_ano_nascimento)

ano_perguntado = int(input("Digite o ano de nascimento:"))
calcular_idade(ano_perguntado)
