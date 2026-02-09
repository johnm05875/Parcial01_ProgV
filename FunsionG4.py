# Función que recibe una lista y retorna el número de elementos que contiene
#*********************************
#** Desarrollado por: Freinanyelis Gomez        ID: 159935684 **
#*****************************************
def contar_elementos(lista):
   return len(lista)

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese elementos separados por espacio: ")
lista_elementos = entrada.split()
resultado = contar_elementos(lista_elementos)
print("freinanyelis gomez - Resultado de la función:", resultado)

#Lista-contenido
#*********************************
#** Desarrollado por: John Miró  ID: 10-715-2197 **
#******************************************************
def valor_minimo(lista):
    if len(lista) == 0:
        return None  # Evita error si la lista está vacía
    return min(lista)


# Ejemplo de uso
numeros = [5, 3, 8, 1, 9]
minimo = valor_minimo(numeros)
print("El valor mínimo es:", minimo)