# Suma de una lista de números
#*********************************
#** Desarrollado por: Freinanyelis Gomez        ID: 159935684 **
#*****************************************

def suma_lista(numeros):
   total = sum(numeros)
   return total

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese varios números separados por espacio: ")
# Convertimos los datos a enteros
lista_numeros = list(map(int, entrada.split()))
resultado = suma_lista(lista_numeros)
print("freinanyelis gomez - Resultado de la función:", resultado)

#Promedio de-lista
#*********************************
#** Desarrollado por: John Miró  ID: 10-715-2197 **
#******************************************************

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0  # Evita división entre cero
    return sum(lista) / len(lista)


# Ejemplo de uso
numeros = [10, 8, 9, 7, 6]
promedio = calcular_promedio(numeros)
print("El promedio es:", promedio)
