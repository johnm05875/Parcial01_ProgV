# Lista Negativos - Lista Positivos
# Desarrollado por: freinanyelis gomez ID 159935684
# Función que recibe una lista de números y retorna solo los números negativos
def obtener_negativos(lista):
   negativos = []
   for numero in lista:
       if numero < 0:
           negativos.append(numero)
   return negativos

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese números separados por espacio: ")
lista_numeros = list(map(int, entrada.split()))
resultado = obtener_negativos(lista_numeros)
print("freinanyelis gomez - Resultado de la función:", resultado)