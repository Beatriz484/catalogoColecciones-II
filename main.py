# main.py

# main.py

from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    remove_piece,
    filter_by_status,
    get_average_price
)

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE CATÁLOGO COLECCIONABLE  ")
    print("========================================")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza por identificador")
    print("6. Eliminar una pieza")
    print("7. Salir")

def main():
    catalog = []
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-7): ").strip()
        
        if opcion == "1":
            print("\n--- Registrar Nueva Pieza ---")
            p_id = input("ID: ")
            name = input("Nombre: ")
            category = input("Categoría: ")
            price = input("Precio: ")
            status = input("Estado (disponible / reservada / vendida): ")
            description = input("Descripción (debe contener 'usada' o 'certificada'): ")
            
            try:
                nueva_pieza = add_piece(p_id, name, category, price, status, description)
                catalog.append(nueva_pieza)
                print("✅ ¡Pieza agregada con éxito al catálogo!")
            except ValueError as e:
                print(f"❌ Error al validar la pieza: {e}")
                
        elif opcion == "2":
            print("\n--- Listado de Piezas ---")
            nombres = list_pieces(catalog)
            if not nombres:
                print("El catálogo está vacío.")
            else:
                for idx, nombre in enumerate(nombres, 1):
                    print(f"{idx}. {nombre}")
                    
        elif opcion == "3":
            print("\n--- Piezas Disponibles ---")
            try:
                disponibles = filter_by_status(catalog, "disponible")
                if not disponibles:
                    print("No hay piezas disponibles actualmente.")
                else:
                    for p in disponibles:
                        print(f"- [{p['id']}] {p['name']} ({p['category']}) -> {p['price']}€")
            except ValueError as e:
                print(f"❌ Error: {e}")
                
        elif opcion == "4":
            print("\n--- Precio Promedio ---")
            try:
                promedio = get_average_price(catalog)
                print(f"💰 El precio promedio del catálogo es: {promedio:.2f}€")
            except Exception as e:
                print(f"❌ Error: {e}")
                
        elif opcion == "5":
            print("\n--- Buscar Pieza por ID ---")
            p_id = input("Introduce el ID a buscar: ")
            pieza = find_piece_by_id(catalog, p_id)
            if pieza:
                print("✅ ¡Pieza encontrada!")
                for clave, valor in pieza.items():
                    print(f"  - {clave}: {valor}")
            else:
                print("🔍 No se encontró ninguna pieza con ese identificador.")
                
        elif opcion == "6":
            print("\n--- Eliminar Pieza ---")
            p_id = input("Introduce el ID de la pieza a eliminar: ")
            try:
                remove_piece(catalog, p_id)
                print("🗑️ ¡Pieza eliminada correctamente del catálogo!")
            except ValueError as e:
                print(f"❌ Error: {e}")
                
        elif opcion == "7":
            print("\n👋 ¡Gracias por usar el sistema de gestión! Hasta pronto.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, selecciona un número entre 1 y 7.")

if __name__ == "__main__":
    main()
    