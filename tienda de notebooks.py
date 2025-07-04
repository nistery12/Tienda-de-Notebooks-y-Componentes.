productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

precios = {
    '8475HD': 387990,
    '2175HD': 327990,
    'JjfFHD': 424990,
    'fgdxFHD': 664990,
    'GF75HD': 749990,
    '123FHD': 290890,
    '342FHD': 444990,
    'UWU131HD': 349990
}
stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0]
}

def stock_por_marca(marca):
    marca_busqueda = input("esribe la marca: ").lower()
    total=0
    for codigo in productos:
        marca = productos[codigo][0].lower()
        if marca == marca_busqueda:
            total == stock[codigo]
    print("El stock total de", marca_busqueda, "es", total)

def busqueda_por_precio():
    p_min = int(input("Precio minimo: "))
    p_max = int(input("Precio maximo: "))
    print("Productos en ese rango de precios: ")
    for codigo in precios:
        if p_min <= precios[codigo] <= p_max and stock[codigo] > 0:
            info = productos[codigo]
            print(f"Modelo: {codigo} | Marca: {info[1]} | Almacenamiento: {info[2]} | Precio: {precios[codigo]} | Stock: {stocks[codigo]}")
    print("")

def actualizar_precio():
    codigo = input("Escribe el codigo del modelo:").strip().upper()
    if codigo in precios:
        nuevo = int(input("Escribe el nuevo precio: "))
        precios[codigo] = nuevo
        print("¡Precio actualizado!\n")
    else:
        print("Modelo no encontrado.\n")

def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock por marca.")
        print("2. buscar por rango de precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Ingrese marca a consultar: ")

        if opcion == "1":
            stock_por_marca()
        elif opcion == "2":
            busqueda_por_precio()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida.")

menu()
        