# Suma de una lista de números
# Desarrollado por: freinanyelis gomez
# Función que recibe una lista de números y calcula la suma total
def suma_lista(numeros):
   total = sum(numeros)
   return total

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese varios números separados por espacio: ")
# Convertimos los datos a enteros
lista_numeros = list(map(int, entrada.split()))
resultado = suma_lista(lista_numeros)
print("freinanyelis gomez - Resultado de la función:", resultado)
