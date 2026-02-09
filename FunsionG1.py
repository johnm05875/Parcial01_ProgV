# Par - Impar

# Desarrollado por: Héctor Lavoe

# Función que recibe un número entero y determina si es par o impar

def par_impar(numero):

    if numero % 2 == 0:

        return "Es par"

    else:

        return "Es impar"


# *********** PRUEBA DE FUNCIONAMIENTO ***********

numero = int(input("Ingrese un número entero: "))

resultado = par_impar(numero)

print("Héctor Lavoe - Resultado de la función:", resultado)
 