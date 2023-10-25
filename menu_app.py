#Funcion agregar compra
def agregar_compra(compras, total_gastado):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print("Compra agregada correctamente.")
    return total_gastado

# Funcion mostrar compras
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras realizadas:")
        for i, monto in enumerate(compras, 1):
            print(f"{i}. ${monto:.2f}")

# Funcion mostrar total gastado
def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")

# Funcion main del ciclo principal
def main():
    compras = []
    total_gastado = 0

#Bucle while
    while True:
        print("\nMenú de Compras")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
#Declaración if
        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
