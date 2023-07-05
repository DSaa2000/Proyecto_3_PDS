
from GameClass import Game
from DBClass import DataBase
from functions import input_select

db = DataBase()

db.ReadFile()

def validGame(game):
    if not isinstance(game.title, str):
        return False
    if game.title == "":
        return False
    if not isinstance(game.priceBuy, int) and not isinstance(game.priceBuy,float):
        return False
    if not isinstance(game.priceSale, int) and not isinstance(game.priceSale, float):
        return False
    if not isinstance(game.count, int):
        return False
    if game.priceBuy <= 0:
        return False
    if game.priceSale <= 0:
        return False
    if game.count <= 0:
        return False
    return True
    
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
    addGameToInventory(id,game)

def addGameToInventory(id,game):
    # agrega el producto a inventario
    if id in db.Inventario:
        juego = db.Inventario[id]
        juego.count += game.count
    else:
        valid = validGame(game)
        if valid:
            db.Inventario[id] = game
            db.updateIndex()
            # agrega el producto al listado de compras
            db.Compras.append(game) 
            print("Notificación: Juego agregado al catálogo con éxito.")
        else:
            print("Notificación: Estructura del juego invalida.")
        
def buyGame():
    juegoSeleccionado = input_select(db.listInventoryToSale(),"Ingrese ID del juego que desea comprar:")
    cantidad = int(input("Cantidad a comprar: "))

    juego, valid, sms = validVenta(juegoSeleccionado,cantidad)
    if valid:
        respuesta = DoSale(juego,cantidad)
        print(respuesta)
    else:
        print("Notificacion:",sms)
def DoSale(juego,cantidad):
    respaldo = juego.count
    juego.count = int(cantidad)
    db.Ventas.append(juego)
    juego.count = int(respaldo) - int(cantidad)        
    db.Inventario[juego.id] = juego
    return "Notificacion: Compra exitosa"
def validVenta(juegoSeleccionado,cantidad):
    estado = True
    juego = {}
    sms = "ok"
    if int(cantidad) <= 0:
        return juego,False,"Ingrese una cantidad mayor que 0"
    for key in db.Inventario:
        juego = db.Inventario[key]
        if juego.DetailSale_Product() == juegoSeleccionado:
            if int(juego.count < int(cantidad):
                estado = False
                sms = "No hay stock suficiente"
            break
                 
    return juego, estado, sms

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
