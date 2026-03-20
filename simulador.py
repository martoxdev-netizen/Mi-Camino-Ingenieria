import random
import string

print("--- GENERADOR DE CONTRASEÑAS PRO (Martox Security) ---")

caracteres = string.ascii_letters + string.digits + string.punctuation
largo = int(input("¿De cuántos caracteres quieres tu contraseña segura?: "))

password = "".join(random.sample(caracteres, largo))

print(f"\nTu contraseña generada es: {password}")

# --- NUEVA LÓGICA DE SEGURIDAD ---
if largo < 8:
    print("Estado: Contraseña DÉBIL (Muy corta)")
elif largo < 12:
    print("Estado: Contraseña MEDIA")
else:
    print("Estado: Contraseña FUERTE (Nivel Ingeniero)")

print("-" * 50)
print("Tip de seguridad: No la compartas con nadie.")