import random

def lanzar_dado():
    return random.randint(1, 6)

print("🎲 ¡Bienvenido al simulador de dados!")

while True:
    input("Presiona Enter para lanzar el dado... ")
    resultado = lanzar_dado()
    
    # Representación visual del dado
    dados = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }

    print(f"🎲 Resultado: {resultado} {dados[resultado]}")
    
    jugar_de_nuevo = input("¿Quieres lanzar otra vez? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        print("¡Gracias por jugar! 👋")
        break
