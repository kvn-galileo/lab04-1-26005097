# Ejercicio #3: (Nombre del archivo: ejercicio3.py)
# Escriba un programa en Python que simule como se va
# gastando la bateria de un telefono. Su simulación debe
# comenzar con la bateria del telefono cargada totalmente,
# al 100%. Despues debe hacer un ciclo que en cada iteración
# genere un numero aleatorio entre 4 y 12, que representará el
# porcentaje de bateria que se descargará. Continue descargando la bateria, 
# hasta que esta se descargue por completo. Por cada iteración debe 
# desplegar cuanto se descargó la bateria y cuanto queda de carga. 
# Al final del programa debe desplegar cuantas iteraciones tomó el descargarla.


import random
import math

battery = 100
iterations = 0

print("lost: %", 0, "current: %", battery)

while True:
    iterations += 1
    lost_battery = random.randint(4, 12)
    lost_percentage = math.ceil((lost_battery * battery) / 100)
    battery -= lost_percentage

    print("lost: %", lost_percentage, "current: %", battery)

    if (battery <= 0):
        break

    
print("Iteraciones: ", iterations)
