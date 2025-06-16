"""
Acciones del menú:

cambiar listas por diccionarios[]
cambiar las funciones para que se usen diccionarios[]
busqueda de diccionarios dentro de lista
agregar el procesamiento de codigos de productos
"""
opcion=0

lista_productos=[]
#producto={"nombre":nombre,"cantidad":stock,"precio":precio}


def solicitarproducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
           return[nombreProd,precioProd,stockProd]
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):
    for producto in lista_productos:
        if producto["nombre"].lower()==nombre.lower():
            return producto
    return None

def guardarproducto(nombre,precio,stock):
    if buscarProducto(nombre)==None:
        producto={
            "nombre":nombre,
            "cantidad":stock,
            "precio":precio
                  }
        lista_productos.append(producto)
        print("producto guardado con exito")
    else:
        print(" ya existe un producto con ese nombre")


def actualizarproducto(nombre, nuevoPrecio, nuevoStock):
    productobuscado=buscarProducto(nombre)
    if productobuscado!=None:
        indice=lista_productos.index(productoEncontrado)
        productobuscado["precio"]=nuevoPrecio
        productobuscado["cantidad"]=nuevoStock

        lista_productos[indice]=productobuscado
        print(f"el producto {nombre} fue actualizado correctamente")
    else:
        print("el preoducto no exixte")

def mostrarinventariocompleto():
    if len(lista_productos)==0:
        print("no hay productos registrado")

    else:
        for producto in lista_productos:
            print(f"Nombre: {producto["nombre"]}, Precio: ${producto["precio"]}, Stock: {producto["cantidad"]}")

def eliminarproducto(nombre):
    productobuscado=buscarProducto(nombre)
    if productobuscado!=None:
        lista_productos.remove(productobuscado)
        print("producto eliminado correctamente")
    else:
        print("el producto no existe")

while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            infoproducto=solicitarproducto()
            if infoproducto!=None:
                guardarproducto(infoproducto[0],
                                infoproducto[1],
                                infoproducto[2])

        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ").lower()
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print(f"Nombre: {productoEncontrado["nombre"]} \t\t Precio: ${productoEncontrado["precio"]} \t\t Stock: {productoEncontrado["cantidad"]}")
                print("-"*60)
            
        case "3":
            infoproducto=solicitarproducto()
            if infoproducto!=None:
                actualizarproducto(nombre=infoproducto[0], nuevoPrecio=infoproducto[1], nuevoStock=infoproducto[2])


        case "4":
            print("-"*70)
            mostrarinventariocompleto()
            print("-"*70)

        case "5":
            nombre=input("Ingrese el nombre del producto a eliminar: ")
            eliminarproducto(nombre)

        case "6":
            print("saliendo del sistema...")

        case default:
            print("opcion no valida")
