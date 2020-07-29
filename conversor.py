def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
    return

menu = """
Bienvenido al conversor de monedas 👑

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
    # pesos = input("Cuantos pesos colombianos tienes?: ")
    # pesos = float(pesos)
    # valor_dolar = 3875
    # dolares = pesos / valor_dolar
    # dolares = round(dolares, 2)
    # dolares = str(dolares)
    # print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    conversor("argentinos", 65)
    # pesos = input("Cuantos pesos argentinos tienes?: ")
    # pesos = float(pesos)
    # valor_dolar = 65
    # dolares = pesos / valor_dolar
    # dolares = round(dolares, 2)
    # dolares = str(dolares)
    # print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    conversor("mexicanos", 24)
    # pesos = input("Cuantos pesos mexicanos tienes?: ")
    # pesos = float(pesos)
    # valor_dolar = 24
    # dolares = pesos / valor_dolar
    # dolares = round(dolares, 2)
    # dolares = str(dolares)
    # print("Tienes $" + dolares + " dolares")
else:
    print('Ingresa una opcion correcta por favor.')