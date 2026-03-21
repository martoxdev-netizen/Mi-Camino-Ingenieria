# --- PROYECTO 2: CIFRADOR DE MENSAJES (Martox Security) ---

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        
        # Cifrar letras mayúsculas
        if char.isupper():
            resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
        # Cifrar letras minúsculas
        elif char.islower():
            resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)
        # Mantener espacios y símbolos igual
        else:
            resultado += char
    return resultado

print("=== SISTEMA DE CIFRADO CÉSAR V1.0 ===")
mensaje = input("Escribe el mensaje secreto: ")
llave = int(input("Ingresa el nivel de cifrado (ej: 3): "))

mensaje_seguro = cifrar_cesar(mensaje, llave)

print(f"\n--- MENSAJE ENCRIPTADO ---")
print(mensaje_seguro)
print("-" * 30)
print("¡Solo quien tenga la llave podrá leerlo!")