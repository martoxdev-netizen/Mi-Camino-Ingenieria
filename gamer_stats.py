# --- PROYECTO 3: GAMER LEVEL SYSTEM (Martox Dev) ---

import time

def calcular_nivel(xp):
    # Cada nivel pide 100 de XP
    return (xp // 100) + 1

print("=== INICIANDO SISTEMA GAMER V1.0 ===")
nombre_jugador = input("Ingresa tu Nickname: ")
print(f"Bienvenido al servidor, {nombre_jugador}!")

# Base de datos local simple
stats = {
    "partidas_ganadas": 0,
    "xp_total": 0,
    "rango": "Bronce"
}

while True:
    print(f"\n[STATS ACTUALES] XP: {stats['xp_total']} | NIVEL: {calcular_nivel(stats['xp_total'])}")
    accion = input("\n¿Qué hiciste hoy? (gane / perdi / exit): ").lower()

    if accion == "gane":
        print("¡GG! Ganaste +50 XP")
        stats["xp_total"] += 50
        stats["partidas_ganadas"] += 1
    elif accion == "perdi":
        print("F... pero ganaste +10 XP por el esfuerzo.")
        stats["xp_total"] += 10
    elif accion == "exit":
        print("Saliendo del sistema... ¡Nos vemos en el lobby!")
        break
    else:
        print("Comando no reconocido, intenta de nuevo.")

    # Lógica de Rangos
    nivel = calcular_nivel(stats['xp_total'])
    if nivel > 10:
        stats["rango"] = "Diamante"
    elif nivel > 5:
        stats["rango"] = "Oro"

    print(f"RANGO ACTUAL: {stats['rango']}")
    time.sleep(1) # Pausa dramática