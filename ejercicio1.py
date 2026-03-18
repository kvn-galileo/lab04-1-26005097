# Ejercicio #1: (Nombre del archivo: ejercicio1.py)
# Para este ejercicio deberá escribir un programa que simule un algoritmo
# de verificación de PIN en un ATM (Cajero). El validador solo permitirá al usuario ingresar
# el PIN correcto 4 veces, si no lo ingresa en los 4 intentos, debe desplegar
# un error final "Se le acabaron los intentos, vuelva mas tarde" y finalizar.
# El validador tiene que verificar antes que nada que el PIN ingresado sea un numero de
# 4 digitos, luego verificar que sea el correcto (defina un numero fijo dentro de su programa
# que reconozca como corecto, usted decide cual), si el numero es correcto, para el programa
# con un mensaje que comunique que el pin fue correcto y si no, permite un siguiente intento.

PASSWORD = "1234"
attemps = 0

while True:
    try:

        if (attemps == 4):
            print("You have tried many attemps, contact suport to recover your password.")
            break

        guess = input("PIN: ")

        guess_lenght = len(guess)
        is_a_number = bool(int(guess))

        if guess_lenght != 4:
            attemps += 1
            print("Incorrect password.")
            continue


        if guess == PASSWORD:
            print("Your password is correct. Here is your money.")
            print("Q 0.01")
            break
        

        if (guess != PASSWORD and attemps <= 4):
            attemps += 1
            print("Incorrect password.")

            continue


    except:
        print("Value is not a number.")



