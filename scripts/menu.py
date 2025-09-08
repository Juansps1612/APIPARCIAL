import requests
import json

API_URL = "http://localhost:5000/jugadores"  # Ajusta si cambias de host/puerto

def listar_jugadores():
    res = requests.get(API_URL)
    if res.status_code == 200:
        jugadores = res.json()
        if jugadores:
            print("\n📋 Lista de jugadores:")
            for j in jugadores:
                print(f"{j['id']}: {j['nombre']} | {j['equipo']} | {j['posicion']} | {j['edad']} años | {j['nacionalidad']}")
        else:
            print("⚠️ No hay jugadores registrados.")
    else:
        print("❌ Error al obtener jugadores.")

def agregar_jugador():
    nombre = input("Nombre: ")
    equipo = input("Equipo: ")
    posicion = input("Posición: ")
    edad = input("Edad: ")
    nacionalidad = input("Nacionalidad: ")

    jugador = {
        "nombre": nombre,
        "equipo": equipo,
        "posicion": posicion,
        "edad": int(edad),
        "nacionalidad": nacionalidad
    }

    res = requests.post(API_URL, json=jugador)
    respuesta = res.json()
    
    if res.status_code == 201:
        print(f"✅ Jugador '{nombre}' agregado correctamente.")
    else:
        # Aquí mostramos el mensaje de error que devuelve el backend
        if "error" in respuesta:
            print(f"⚠️ {respuesta['error']}")
        else:
            print("⚠️ Ocurrió un error desconocido al agregar el jugador.")
def eliminar_jugador():
    jugador_id = input("ID del jugador a eliminar: ")
    res = requests.delete(f"{API_URL}/{jugador_id}")
    if res.status_code == 200:
        print("🗑️ Jugador eliminado correctamente.")
    else:
        error = res.json().get("error", "Error desconocido")
        print(f"⚠️ {error}")

def actualizar_jugador():
    jugador_id = input("ID del jugador a actualizar: ")

    nombre = input("Nuevo nombre (enter para mantener): ")
    equipo = input("Nuevo equipo (enter para mantener): ")
    posicion = input("Nueva posición (enter para mantener): ")
    edad = input("Nueva edad (enter para mantener): ")
    nacionalidad = input("Nueva nacionalidad (enter para mantener): ")

    jugador = {}
    if nombre: jugador["nombre"] = nombre
    if equipo: jugador["equipo"] = equipo
    if posicion: jugador["posicion"] = posicion
    if edad: jugador["edad"] = int(edad)
    if nacionalidad: jugador["nacionalidad"] = nacionalidad

    res = requests.put(f"{API_URL}/{jugador_id}", json=jugador)
    if res.status_code == 200:
        print("✅ Jugador actualizado correctamente.")
    else:
        error = res.json().get("error", "Error desconocido")
        print(f"⚠️ {error}")

def menu():
    while True:
        print("\n=== MENÚ DE JUGADORES ===")
        print("1. Listar jugadores")
        print("2. Agregar jugador")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_jugadores()
        elif opcion == "2":
            agregar_jugador()
        elif opcion == "3":
            actualizar_jugador()
        elif opcion == "4":
            eliminar_jugador()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
