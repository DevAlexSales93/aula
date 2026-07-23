import math

def unir_nomes(nome, sobrenome):
    # ! soma de textos = CONCATENAÇÃO
    nome_completo = nome + "" + sobrenome

    print("O nome completo é: ", nome_completo)

unir_nomes("Cuca", "Beludo")

# ! a diferença entre função 'com resultado' e função 'sem resultado'

potencia = math.pow(25, 5)
print("A potência é:", potencia)
nome = unir_nomes("Mudrungo", "Souza")
print("O nome é:", nome)

#? string replace
pais = "Brasil"
trocado = pais.replace("B", "P")
print("O nome trocado é:", trocado)
