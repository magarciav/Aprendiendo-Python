import random
import string

def generatePassword(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validatePassword():
    while True:
        try:
            password_length = int(input("Ingrese la longitud deseada para la contraseña: "))
            if password_length < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
            elif password_length > 40:
                print("La contraseña debe ser menor o igual a 40 caracteres.")
            else:
                new_password = generatePassword(password_length)
                print("Contraseña generada:", new_password)
                return True
        except ValueError as e:
            print(f"Error: {e}")

validatePassword()
