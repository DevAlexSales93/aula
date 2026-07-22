def converter_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"\nTemperatura em Fahrenheit: {fahrenheit:.2f}°F")

celsius = float(input("Digite a temperatura em graus celsius: ").replace(",", "."))   

converter_fahrenheit(celsius)