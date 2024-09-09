import math
 
def sumar(x, y):
    return x + y
def restar(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero."
 
def calcular_factorial(m):
    if isinstance(m, int) and m >= 0:
        return math.factorial(m)
    else:
        return "El factorial no está definido para números negativos o no enteros."
 
def mostrar_opciones():
    print("\na. Suma")
    print("b. Resta")
    print("c. Multiplicación")
    print("d. División")
    print("s. Salir")
 
def realizar_calculo(seleccion, x, y):
    if seleccion == 'a':
        resultado = sumar(x, y)
    elif seleccion == 'b':
        resultado = restar(x, y)
    elif seleccion == 'c':
        resultado = multiplicar(x, y)
    elif seleccion == 'd':
        resultado = dividir(x, y)
    else:
        return "Opción no válida."
 
    if isinstance(resultado, (int, float)) and resultado == int(resultado):
        fact_resultado = calcular_factorial(int(resultado))
        return f"{x} {'+' if seleccion == 'a' else '-' if seleccion == 'b' else '*' if seleccion == 'c' else '/'} {y} = {resultado}\nFactorial de {int(resultado)} = {fact_resultado}"
    else:
        return f"Resultado: {resultado}"
 
def iniciar_programa():
    while True:
        numero1 = int(input("Ingrese el primer número:\t"))
        numero2 = int(input("Ingrese el segundo número:\t"))
       
        mostrar_opciones()
        seleccion = input("Ingrese la opción:\t").lower()
       
        if seleccion == 's':
            print("Saliendo del programa...")
            break
       
        print(realizar_calculo(seleccion, numero1, numero2))
        print()
       
iniciar_programa()
