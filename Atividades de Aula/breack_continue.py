contador = 0
maximo = 50

while contador < maximo:
    contador += 1
    if contador % 4 == 0:
        continue    
    print(contador)
    if contador == 38:
        break

print(contador)
print("Fim do Contador")
    