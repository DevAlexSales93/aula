def verificar_velocidade(velocidade, limite):
    if velocidade <= limite:
        print("\nVelocidade permitida!")
    else:
        excesso = velocidade - limite
        print("\nVelocidade acima do permitido!")        
        print(f"\nVocê ultrapassou o limite em {excesso:.0f} km/h.")

velocidade = float(input("Digite a velocidade do veículo (km/h):"))       
limite = float(input("Digite o limite da via (km/h):").replace(",", "."))

verificar_velocidade(velocidade, limite)