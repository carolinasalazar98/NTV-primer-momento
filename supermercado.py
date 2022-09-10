productos=[]
superMercado=1

while superMercado:
    opcion = (int(input("""
    -----MENU-----------
    1. Ingresar producto
    2. Mostrar productos
    3. Buscar por código un producto y editar el precio
    4. Buscar por código un producto y eliminar el producto
    0. SALIR
    """)))
    if opcion == 1:
        producto={}
        codigo= (int(input("Digite el codigo del producto: "))) 
        nombre= (input("Digite el nombre del producto: "))
        precio= (float(input("Digite el precio del producto: ")))
        producto['codigo']=codigo
        producto['nombre']=nombre
        producto['precio']=precio

        productos.append(producto)

    elif opcion == 2:
        print(productos)

        for i in productos:
            print(f"Codigo producto: {i['codigo']}")
            print(f"Nombre: {i['nombre']}")
            print(f"Precio: {i['precio']}")
            
    elif opcion == 3:
        buscar=int(input("Digite el codigo del producto: "))
        encontrado=False

        for i in productos:
            if i['codigo'] ==buscar:
                precio=float(input(f"Digite el precio nuevo del producto: {i['nombre']}: "))
                i['precio']=precio
                print("El precio del producto se modifico con exito")
                encontrado=True

                if not encontrado:
                    print("No se encontro el producto")
                     

    elif opcion == 4:
         buscar= int(input("Codigo del producto: "))
         encontrado=False

         for i in productos:
            if i[codigo]==buscar:
             productos.pop(productos.index(i))
             print("Producto Eliminado con exito")
             encontrado=True

             if not encontrado:
                    print("No se encontro el producto")
    
    elif opcion == 0:
         superMercado=0

else:
    print("Digite una opcion correcta")







                






