inventario = [] # Lista donde se almacenará los valores obtenidos en producto

#Realizar validaciones para los respectivos campos 
def agregar_producto():
    print("\nIngrese los datos del producto\n")

    while True:
        name = input("Nombre: ").strip().upper()
        if not name:
            print("El campo no puede quedar vacío")
            continue
        elif not name.replace(" ", "").isalpha():
            print("por favor ingresa solo texto")
            continue
        
        break

    while True:      
        price = (input("Precio: "))
        if not price:
            print("El campo no puede quedar vacío")
            continue

        try: 
            price = float(price)
        except ValueError:
            print("Debe ingresar un número")
            continue
        if price <= 0:
            print("El precio debe ser mayor a 0")
            continue

        break

    while True:
        ammount = input("Cantidad: ")
        if not ammount:
            print("El campo no puede quedar vacío")
            continue

        try: 
            ammount = int(ammount)
        except ValueError:
            print("Debe ingresar un número")
            continue
        if ammount <= 0:
            print("La cantidad debe ser mayor a 0")
            continue

        break

    producto = {
        "Nombre" : name,
        "Precio" : price,
        "Cantidad" : ammount
    }

    inventario.append(producto)
    print("El producto se agregó correctamente")

#Mostrar los productos almacenado en inventario de forma ordenada
def mostrar_inventario():
    if not inventario:
        print("\nNo hay productos en el inventario")
    else:
        print("\n--Productos que se encuentran en el inventario--\n")
    for item in inventario:
        print(f"Nombre: {item['Nombre']} | Precio: {item['Precio']} | Cantidad: {item['Cantidad']}")

#Calcular el valor total de todos los productos y cuántos de estos hay
def calcular_estadistica():
    # Total del inventario
    valor_total_inventario = sum(
        item['Precio'] * item['Cantidad']
        for item in inventario
    )
    print(f"El valor total del inventario es: {valor_total_inventario}")

    # Cantidad total de productos
    cantidad_productos_registrados = sum(
        item['Cantidad']
        for item in inventario
    )

    print(f"Usted tiene {cantidad_productos_registrados} producto(s) registrados.")
    

#Menú que pregunta constantemente al usuario que acción desea realizar y sus respectivas validaciones
option = 0

while option != 4:
    print("\n----------Inventario----------")

    print("\nSelecione el número según la opción que desee elegir")

    print("\nSelecciona la opción que necesite " 
    "\n1. Agregar producto " 
    "\n2. Mostrar inventario" 
    "\n3. Calcular estadísticas"
    "\n4. Salir")

    try:
        option = int(input("Ingrese la opción: "))

        if option not in range(1,4+1):
            print("\nSeleccione una opción dentro del rango")
            continue
    except ValueError:
        print("\nValor no válido, por ingrese el numero acorde a su opción")
        continue

    if option == 1:
        agregar_producto()
    elif option == 2:
        mostrar_inventario()
    elif option == 3:
        calcular_estadistica()
    elif option == 4:
        print("\nSaliendo del programa... ¡Hasta luego!\n")
                                        