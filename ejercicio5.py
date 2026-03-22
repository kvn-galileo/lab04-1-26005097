# Ejercicio #5: (Nombre del archivo: ejercicio5.py)
# Para este ejercicio se le pide que: (1) lea una palabra de el usuario,
# (2) lea una letra de el usuario, (3) busque la letra dentro de la palabra,
# identifique en donde se encuentran y despues despliegue cada letra de la palabra,
# separadas por espacios, reemplazando por _ las letras que no sean igual a la que leyó.
# Ejemplos:

# 		Ejemplos #1:
# 		Ingrese palabra: cuadrado
# 		Letra a buscar: a
# 		Resultado busqueda: _ _ a _ _ a _ _

# 		Ejemplos #2:
# 		Ingrese palabra: pantalla
# 		Letra a buscar: l
# 		Resultado busqueda: _ _ _ _ _ l l _
word = input('Ingrese palabra: ')
letter = input('Letra a buscar: ')

new_str = ''

index = 0
while index <= len(word) - 1:
    current = word[index]

    if current == letter:
        new_str += letter
    else:
        new_str += '_'
    
    index += 1

print(new_str)
