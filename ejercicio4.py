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

first_attempt = True
valid_length = False
has_vowels = False
has_digits = False

while True:
    mark_lenght = "x" if valid_length else " "
    mark_vowels = "x" if has_vowels else " "
    mark_numbers = "x" if has_digits else " "

    verification_message = f"""
      (1) Tener por lo menos 8 caracteres [{mark_lenght}]
      (2) Contenga mas de una vocal       [{mark_vowels}]
      (3) Contenga mas de un digito       [{mark_numbers}]
    """

    print(verification_message)

    if not first_attempt:
      print('Weak password \n')

    password = input("Password: ")

    valid_length = len(password) >= 8

    str_count = 0
    for letter in password:
      lower_vowel = letter.lower()
      
      if lower_vowel == 'a' or lower_vowel == 'e' or lower_vowel == 'i' or lower_vowel == 'o' or lower_vowel == 'u':
        str_count += 1

      if (str_count > 1):
        has_vowels = True
        break
    
    if str_count <= 1:
      has_vowels = False


    digit_count = 0
    for letter in password:
      if letter.isdigit():
        digit_count += 1
      
      if digit_count > 1:
        has_digits = True
        break
    
    if digit_count <= 1:
      has_digits = False

    invalid_password = password
    validations = valid_length and has_vowels and has_digits

    if validations:
      break
    else:
      first_attempt = False

mark_lenght = "x" if valid_length else " "
mark_vowels = "x" if has_vowels else " "
mark_numbers = "x" if has_digits else " "
verification_message = f"""
      Tu password debe:
      (1) Tener por lo menos 8 caracteres [{mark_lenght}]
      (2) Contenga mas de una vocal       [{mark_vowels}]
      (3) Contenga mas de un digito       [{mark_numbers}]
    """
print(verification_message)
message = 'Strong password.'
print(message)