print('=-==-=-=-=-=-=-=-=-=CONVESOR DE TEMPERATURA=-=-=-==-=-=--=-=-=-=-=')

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade (C, F, K): ").upper()

if unidade == "C":
    print(f"{temperatura}°C em Fahrenheit é {celsius_para_fahrenheit(temperatura)}°F")
    print(f"{temperatura}°C em Kelvin é {celsius_para_kelvin(temperatura)}K")
elif unidade == "F":
    print(f"{temperatura}°F em Celsius é {fahrenheit_para_celsius(temperatura)}°C")
    print(f"{temperatura}°F em Kelvin é {fahrenheit_para_kelvin(temperatura)}K")
elif unidade == "K":
    print(f"{temperatura}K em Celsius é {kelvin_para_celsius(temperatura)}°C")
    print(f"{temperatura}K em Fahrenheit é {kelvin_para_fahrenheit(temperatura)}°F")
else:
    print("Unidade inválida!!!")
