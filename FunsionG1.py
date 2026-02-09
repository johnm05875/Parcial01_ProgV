# Par - Impar
#*********************************
#** Desarrollado por: Freinanyelis Gomez        ID: 159935684 **

#*****************************************
def par_impar(numero):

    if numero % 2 == 0:

        return "Es par"

    else:

        return "Es impar"


# *********** PRUEBA DE FUNCIONAMIENTO ***********

numero = int(input("Ingrese un número entero: "))

resultado = par_impar(numero)

print("Héctor Lavoe - Resultado de la función:", resultado)

 
 
#Mayor-numero
#*********************************
#** Desarrollado por: John Miró  ID: 10-715-2197 **

#*****************************************
def mayor_de_dos(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Ejemplo de uso
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = mayor_de_dos(a, b)
print("El número mayor es:", resultado)



