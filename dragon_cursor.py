# --- PROYECTO 4: SIMULACIÓN DE FÍSICA DE COLA (Inspirado en Dragón Art) ---

import os
import time
import sys

# Módulo para leer el teclado en tiempo real sin pulsar Enter
import msvcrt 

# Parámetros del Dragón
LARGO_CUERPO = 15
caracteres_cuerpo = {
    "cabeza": "🐉",
    "espina": "◌",
    "aleta": "彡"
}

# La terminal tiene 80 columnas de ancho
ANCHO_TERMINAL = 70

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Puntero inicial
puntero_x = ANCHO_TERMINAL // 2
# La cola empieza toda en la misma posición que el puntero
cola = [[puntero_x, 0] for _ in range(LARGO_CUERPO)]

print("\n--- SIMULADOR DE FÍSICA DE COLA ---")
print("Usa 'A' para izquierda y 'D' para derecha (MSVCRT activa).")
print("Presiona ESC para salir.\n")
time.sleep(2)

while True:
    # 1. Leer la entrada del teclado si hay una
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla == b'\x1b': # ESC para salir
            break
        elif tecla == b'a' or tecla == b'A':
            puntero_x = max(0, puntero_x - 3) # Mover puntero
        elif tecla == b'd' or tecla == b'D':
            puntero_x = min(ANCHO_TERMINAL - 1, puntero_x + 3)

    # 2. Física de Interpolación: La cola sigue a la cabeza
    # Actualizar la cabeza
    cola[0] = [puntero_x, 0]
    
    # Cada segmento sigue al anterior
    for i in range(1, LARGO_CUERPO):
        # Mover cada segmento un poco más lento (interpolación)
        cola[i][0] += (cola[i-1][0] - cola[i][0]) * 0.7

    # 3. Dibujar en la terminal
    linea = [" "] * ANCHO_TERMINAL
    for i in range(LARGO_CUERPO - 1, -1, -1):
        x = int(cola[i][0])
        # Asegurarse de no dibujar fuera de los bordes
        if 0 <= x < ANCHO_TERMINAL:
            # Asignar caracteres según la posición
            if i == 0:
                linea[x] = caracteres_cuerpo["cabeza"]
            elif i % 5 == 0:
                linea[x] = caracteres_cuerpo["aleta"]
            else:
                linea[x] = caracteres_cuerpo["espina"]

    # Imprimir y forzar actualización
    sys.stdout.write("".join(linea) + "\r")
    sys.stdout.flush()

    time.sleep(0.03) # Pequeña pausa para simular el delay de la cola

print("\n\nSaliendo del simulador... ¡GG!")