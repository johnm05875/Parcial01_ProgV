# Lista - Máximo - Lista factorial
# Desarrollado por: freinanyelis gomez
# Función que recibe una lista y retorna el valor máximo
def valor_maximo(lista):
   return max(lista)

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese números separados por espacio: ")
lista_numeros = list(map(int, entrada.split()))
resultado = valor_maximo(lista_numeros)
print("freinanyelis gomez - Resultado de la función:", resultado)