
from GameClass import Game
from DBClass import DataBase
from functions import input_select

db = DataBase()

db.ReadFile()

    
def registerGame():
    print("Ingrese los datos del nuevo juego:")
    title = str(input("Título: "))
    priceBuy = input("Precio de Compra: ")
    priceSale = input("Precio de Venta: ")
    genero = input_select(db.Generos,"Seleccione un género:")
    platform = input_select(db.Plataformas,"Selecciona una plataforma:")
    cant = input("Cantidad: ")

    id = db.index
    game = Game(id,title,priceBuy,priceSale,genero,platform,cant)
    # agrega el producto a inventario
    db.Inventario[id] = game
    db.updateIndex()
    # agrega el producto al listado de compras
    db.Compras.append(game)
def buyGame():
    juegoSeleccionado = input_select(db.Inventario,"Ingrese ID del juego que desea comprar:")
    cantidad = input("Cantidad a comprar")
  
    return

perfilActual = input_select(db.Perfiles,"Seleccione tipo de usuario:")

def show_MenuAdmin():
    opciones = ["Registrar producto","Ver catálogo de juegos", "Generar reporte","Cerrar sesión"]
    opcion = input_select(opciones,"\n¿Que desea hacer?")
    if opcion == opciones[0]:
        # Registrar producto
        registerGame()
    elif opcion == opciones[1]:
        # Ver catalogo
        print("Catálogo:")
        db.showInventory()
    elif opcion == opciones[2]:
        # Reporte
        db.reportTXT()
    elif opcion == opciones[3]:
        # Exit
        db.Save()
        exit(0)
    show_MenuAdmin()
def show_MenuCliente():    
    opciones = ["Comprar producto","Cerrar sesión"]
    opcion = input_select(opciones,"\n¿Que desea hacer?")
    if opcion == opciones[0]:
        # Registrar producto
        buyGame()
    elif opcion == opciones[1]:
        # Exit
        db.Save()
        exit(0)
    show_MenuCliente()

if perfilActual == "Administrador":
    show_MenuAdmin()
else:
    show_MenuCliente()
