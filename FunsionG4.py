# Lista - Número - Lista contenido
# Desarrollado por: freinanyelis gomez
# Función que recibe una lista y retorna el número de elementos que contiene
def contar_elementos(lista):
   return len(lista)

# *********** PRUEBA DE FUNCIONAMIENTO ***********
entrada = input("Ingrese elementos separados por espacio: ")
lista_elementos = entrada.split()
resultado = contar_elementos(lista_elementos)
print("freinanyelis gomez - Resultado de la función:", resultado)