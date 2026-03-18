# Ejercicio #2: (Nombre del archivo: ejercicio2.py)
# Para este ejercicio se le pide que implemente lo siguiente:
# Un programa que dado un String leido del usuario, cree una copia
# del String, pero con los siguientes reemplazos:

# (1) Pase todos los caracteres en mayusculas - 
# Para esto si puede utilizar funciones en Python que haga el
# trabajo en una sola llamada

# (2) Reemplazar caracteres der la siguiente forma:
# 			letra A , reemplazar por un 4
# 			letra E, reemplazar por un 3
# 			letra I, reemplazar por un 1
# 			letra O, reemplazar por un 0

user_str = input("Ingrese su string: ")
new_str = ""

for letter in user_str.upper():
    if letter == 'A':
        new_str += '4'
    elif letter == 'E':
        new_str += '3'
    elif letter == 'I':
        new_str += '1'
    elif letter == 'O':
        new_str += '0'
    else:
        new_str += letter


print(new_str)
    



