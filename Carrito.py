class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto}' agregado al carrito.")

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto}")

    def vaciar_carrito(self):
        self.productos = []
        print("Carrito vaciado.")


# Función principal para probar el carrito de compras
def main():
    carrito = CarritoDeCompras()

    while True:
        print("\n1. Agregar producto al carrito")
        print("2. Mostrar contenido del carrito")
        print("3. Vaciar carrito")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a agregar: ")
            carrito.agregar_producto(producto)
        elif opcion == '2':
            carrito.mostrar_carrito()
        elif opcion == '3':
            carrito.vaciar_carrito()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == '__main__':
    main()
