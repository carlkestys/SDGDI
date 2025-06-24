#concierto_python

lista_compradores=[]

opcion=0

def solicitarentrada():
    nombrecomprador= input("Ingrese el nombre del comprador: ")
    try:
        tipoentrada=input("ingrese el tipo de entrada(v/g): ")
        codigo=input("Ingrese el codigo de acceso: ")
        if codigo!="Acceso123":
            print("codigo erroneo intente de nuevo")
        elif codigo=="Acceso123":
            print("codigo correcto!")
            if tipoentrada!="v":
                raise ValueError
            else:
                return[nombrecomprador,tipoentrada]
    except TypeError:
        print("ingrese un tipo de entrada valido (V/G)")

def guardarcomprador(nombre,tipoentrada): 
    if buscarcomprador(nombre) == None:
        comprador = {"nombre" : nombre,"tipo de entrada" : tipoentrada} 
        lista_compradores.append(comprador)
        print("la entrada se registra exitosamente.")
    else:
        print("Ya existe un comprador con el mismo nombre")
    
def buscarcomprador(nombre):
    for compradores in lista_compradores:
        if compradores["nombre"]==nombre:
            return compradores

def cancelarentrada(nombre_comprador): 
    compradorBuscado = buscarcomprador(nombre_comprador)
    if compradorBuscado != None:
        lista_compradores.remove(compradorBuscado)
        print("entrada cancelada.")
    else:
        print("No existe ningun comprador con ese nombre.")

while opcion!= "4":
    print("**************MENU PRINCIPAL**************")
    print("1.- comprar entrada")
    print("2.- Buscar comprador")
    print("3.- cancelar entrada")
    print("4.- Salir")

    opcion= input("Ingrese la opción que desea(1-4): ")

    match opcion:
        case "1":
            infocomprador = solicitarentrada()
            if infocomprador != None:
                guardarcomprador(infocomprador[0],infocomprador[1])

        case "2":
            nombre=input("Ingrese el nombre del comprador que desea buscar: ")
            compradorencontrado=buscarcomprador(nombre)
            if compradorencontrado!=None:
                print("-" * 60)
                print(f"nombre: {compradorencontrado["nombre"]}")
                print(f"tipo de entrada: {compradorencontrado["tipoentrada"]}")
                print("-" * 60)
            else:
                print("No existe ningun comprador con ese nombre.")

        case "3":
            nombre=input("Ingrese el nombre del cliente que quiere cancelar su entrada: ")
            cancelarentrada(nombre)

        case "4":
            print("Saliendo del programa...")

        case default:
            print("Opcion no valida.")