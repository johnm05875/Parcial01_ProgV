# Cadena - Número - Cadena vacía
#*********************************
#** Desarrollado por: Freinanyelis Gomez        ID: 159935684 **
#*****************************************
def contar_caracteres(cadena):
   return len(cadena)

# *********** PRUEBA DE FUNCIONAMIENTO ***********
texto = input("Ingrese una cadena de texto: ")
resultado = contar_caracteres(texto)
print("freinanyelis gomez - Resultado de la función:", resultado)


#Cadena-Vacía
#*********************************
#** Desarrollado por: John Miró  ID: 10-715-2197 **
#******************************************************
def cadena_vacia(cadena):
    if cadena == "":
        return True
    else:
        return False


# Ejemplo de uso
texto = input("Ingrese una cadena de texto: ")

if cadena_vacia(texto):
    print("La cadena está vacía")
else:
    print("La cadena NO está vacía")
