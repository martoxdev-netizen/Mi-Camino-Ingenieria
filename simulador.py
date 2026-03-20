import random
import string

print("--- GENERADOR DE CONTRASEÑAS PRO (Martox Security) ---")

# Definimos los caracteres que puede usar la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Pedimos al usuario el largo de la clave
largo = int(input("¿De cuántos caracteres quieres tu contraseña segura?: "))

# Generamos la clave mezclando caracteres al azar
password = "".join(random.sample(caracteres, largo))

print(f"\nTu contraseña generada es: {password}")
print("-" * 50)
print("Tip de seguridad: No la compartas con nadie.")