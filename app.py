from dao.trabajo_dao import TrabajoDAO
from models.trabajo import Trabajo

dao = TrabajoDAO()


def mostrar():
    trabajos = dao.obtener_todo()
    print("\n===A TRABAJOS ===")
    for t in trabajos:
        print(f"{t.id} | {t.titulo} | {t.estado}")


def agregar():
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    inicio = input("Fecha inicio: ")
    fin = input("Fecha final: ")
    estado = input("Estado: ")

    trabajo = Trabajo(None, titulo, descripcion, inicio, fin, estado)
    dao.insertar(trabajo)
    print("Agregado")


def actualizar():
    id = int(input("ID: "))
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    inicio = input("Fecha inicio: ")
    fin = input("Fecha final: ")
    estado = input("Estado: ")

    trabajo = Trabajo(id, titulo, descripcion, inicio, fin, estado)
    dao.actualizar(trabajo)
    print("Actualizado")


def eliminar():
    id = int(input("ID: "))
    dao.eliminar(id)
    print("Eliminado")


def menu():
    print("\n=== DEVTRACK ===")
    print("1. Ver trabajos")
    print("2. Agregar trabajo")
    print("3. Actualizar trabajo")
    print("4. Eliminar trabajo")
    print("0. Salir")


def main():
    while True:
        menu()
        op = input("Opción: ")

        if op == "1":
            mostrar()
        elif op == "2":
            agregar()
        elif op == "3":
            actualizar()
        elif op == "4":
            eliminar()
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()