# Lista - Máximo - Lista factorial
# Desarrollado por: freinanyelis gomez        ID: 159935684 **
# Función que recibe una lista y retorna el valor máximo
def valor_maximo(lista):
   return max(lista)

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese números separados por espacio: ")
lista_numeros = list(map(int, entrada.split()))
resultado = valor_maximo(lista_numeros)
print("freinanyelis gomez - Resultado de la función:", resultado)

#Lista-contenido
#*********************************
#** Desarrollado por: John Miró  ID: 10-715-2197 **
#******************************************************
def factorial(numero):
    if numero < 0:
        return None  # El factorial no está definido para negativos
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


# Ejemplo de uso
n = int(input("Ingrese un número: "))
resultado = factorial(n)

if resultado is not None:
    print("El factorial es:", resultado)
else:
    print("El factorial no está definido para números negativos")
