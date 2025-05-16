# -*- coding: utf-8 -*-

plantilla_masculina = {
    "entrenador": ["Hansi Flick"],
    "porteros": ["Ter Stegen", "Iñaki Peña", "Wojciech Szczesny"],
    "defensas": ["Cubarsí", "Balde", "Araujo", "Iñigo Martinez", "christensen", "Kounde", "Eric Garcia"],
    "centrocampistas": ["Frenkie de Jong", "Pedri", "Gavi", "Dani Olmo", "Fermín", "Pablo Torre", "Casadó"],
    "delanteros": ["Lewandowski", "Raphinha", "Ferran Torres", "Lamine Yamal", "Ansu Fati", "Pau Victor"]
}

plantilla_femenina = {
    "entrenador": ["Pere Romeu"],
    "porteros": ["Cata Coll", "Gemma Font", "Roebuck"],
    "defensas": ["Mapi León", "Irene Paredes", "Jana", "Torrejon", "Ona Batlle", "Engen"],
    "centrocampistas": ["Aitana Bonmatí", "Alexia Putellas", "Patri Guijarro", "Kika", "Vicky", "Brugts"],
    "delanteros": ["Caroline Graham Hansen", "Fridolina Rolfö", "Claudia Pina", "Salma Paralluelo", "Ewa Pajor"]
}

once_actual = []

def mostrar_menu():
    print("\n--- GESTOR DE ONCES - FC BARCELONA ---")
    print("1. Ver plantilla masculina")
    print("2. Ver plantilla femenina")
    print("3. Añadir jugador/a al once")
    print("4. Ver once actual")
    print("5. Reiniciar once")
    print("0. Salir")

def mostrar_plantilla(plantilla):
    for posicion, jugadores in plantilla.items():
        print(f"{posicion.capitalize()}: {', '.join(jugadores)}")

def elegir_jugador(plantilla):
    posicion = input("Introduce la posición (porteros, defensas, centrocampistas, delanteros): ").lower()
    if posicion in plantilla:
        print("Jugadores/as disponibles:", ", ".join(plantilla[posicion]))
        nombre = input("Escribe el nombre del jugador/a que quieres añadir: ")
        if nombre in plantilla[posicion]:
            if nombre in once_actual:
                print("Ese jugador/a ya está en el once.")
            elif len(once_actual) < 11:
                once_actual.append(nombre)
                print(f"{nombre} añadido/a al once.")
            else:
                print("Ya hay 11 jugadores/as en el once.")
        else:
            print("Jugador/a no encontrado/a en esa posición.")
    else:
        print("Posición no válida.")

def main():
    plantilla_seleccionada = None

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            plantilla_seleccionada = plantilla_masculina
            print("\n--- Plantilla Masculina ---")
            mostrar_plantilla(plantilla_seleccionada)

        elif opcion == "2":
            plantilla_seleccionada = plantilla_femenina
            print("\n--- Plantilla Femenina ---")
            mostrar_plantilla(plantilla_seleccionada)

        elif opcion == "3":
            if plantilla_seleccionada:
                elegir_jugador(plantilla_seleccionada)
            else:
                print("Primero debes seleccionar una plantilla (opción 1 o 2).")

        elif opcion == "4":
            print("\n--- Once Actual ---")
            if once_actual:
                for i, jugador in enumerate(once_actual, 1):
                    print(f"{i}. {jugador}")
            else:
                print("El once está vacío.")

        elif opcion == "5":
            once_actual.clear()
            print("Once reiniciado.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
