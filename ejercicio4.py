# Ejercicio #4: (Nombre del archivo: ejercicio4.py)
# Escriba un programa que lea del usuario un password,
# hasta que cumpla con las condiciones necesarias para poder ser utilizado.
# Si el password no cumple con las condiciones, debe desplegar "Weak password"
# y pedir que se ingrese otro password. Si el password cumple con la condición,
# debe terminar el programa y desplegar "Strong password".
# Las condiciones que debe cumplir el password son:

# 			(1) Tener por lo menos 8 caracteres
# 			(2) Contenga mas de una vocal
# 			(3) Contenga mas de un digito

valid_lenght = False
has_vowels = False
has_digits = False

validations = not valid_lenght and not has_vowels and not has_digits

while validations:
    veryfication_message = f"""
      (1) Tener por lo menos 8 caracteres [{valid_lenght}]
      (2) Contenga mas de una vocal       [{has_vowels}]
      (3) Contenga mas de un digito       [{has_digits}]
    """    
    print("Type a string password: ")



print(message)