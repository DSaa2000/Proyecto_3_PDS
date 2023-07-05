import unittest
from DBClass import DataBase 
from GameClass import Game
import subprocess
import os

db = DataBase()
db.ReadFile()

# Funciones a probar
def addGameToInventory(id,game):
    # agrega el producto a inventario
    if id in db.Inventario:
        juego = db.Inventario[id]
        juego.count += int(game.count)
    else:
        db.Inventario[id] = game
        db.updateIndex()
        # agrega el producto al listado de compras
    db.Compras.append(game)
def validVenta(juegoSeleccionado,cantidad):
    estado = True
    juego = {}
    sms = "ok"
    if cantidad <= 0:
        return juego,False,"Ingrese una cantidad mayor que 0"
    for key in db.Inventario:
        juego = db.Inventario[key]
        if juego.DetailSale_Product() == juegoSeleccionado:
            if juego.count < cantidad:
                estado = False
                sms = "No hay stock suficiente"
            break                 
    return juego, estado, sms
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

LargoInventario = len(db.Inventario)

class Pruebas(unittest.TestCase):
    # Probar: juego con titulo valido
    def test_validGame_1(self):
        juego = Game(0,"Test_v1",1,1,"Acción","PC",5)
        assert validGame(juego) == True
    # Probar: juego con titulo numerico
    def test_validGame_2(self):
        juego = Game(0,1,1,1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con titulo vacio ""
    def test_validGame_3(self):
        juego = Game(0,"",1,1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de compra valido
    def test_validGame_4(self):
        juego = Game(0,"Test_v4",1,1,"Acción","PC",5)
        assert validGame(juego) == True
    # Probar: juego con precio de compra invalido => no numerico
    def test_validGame_5(self):
        juego = Game(0,"Test_v5","X",1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de compra invalido => menor a 0
    def test_validGame_6(self):
        juego = Game(0,"Test_v6",-1,1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de compra invalido => igual a 0
    def test_validGame_7(self):
        juego = Game(0,"Test_v7",0,1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de venta valido
    def test_validGame_8(self):
        juego = Game(0,"Test_v8",1,1,"Acción","PC",5)
        assert validGame(juego) == True
    # Probar: juego con precio de venta invalido => no numerico
    def test_validGame_9(self):
        juego = Game(0,"Test_v9",1,"X","Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de venta invalido => menor a 0
    def test_validGame_10(self):
        juego = Game(0,"Test_v10",1,-1,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con precio de venta invalido => igual a 0
    def test_validGame_11(self):
        juego = Game(0,"Test_v11",1,0,"Acción","PC",5)
        assert validGame(juego) == False
    # Probar: juego con cantidad valida
    def test_validGame_12(self):
        juego = Game(0,"Test_v12",1,1,"Acción","PC",5)
        assert validGame(juego) == True
    # Probar: juego con cantidad invalida => no numerica
    def test_validGame_13(self):
        juego = Game(0,"Test_v13",1,1,"Acción","PC","X")
        assert validGame(juego) == False
    # Probar: juego con cantidad invalida => menor a 0
    def test_validGame_14(self):
        juego = Game(0,"Test_v14",1,1,"Acción","PC",-1)
        assert validGame(juego) == False
    # Probar: juego con cantidad invalida => igual a 0
    def test_validGame_15(self):
        juego = Game(0,"Test_v15",1,1,"Acción","PC",0)
        assert validGame(juego) == False
    # Probar que se está agregando un producto al inventario y al registro de compras
    def test_AddNewGameToInventory(self):
        id = db.index
        juego = Game(id,"Test",1,1,"Acción","PC",5)
        largoAntes = len(db.Inventario)       
        largoAntesCompras = len(db.Compras)
        addGameToInventory(id,juego)        
        assert largoAntes + 1 == len(db.Inventario) and largoAntesCompras + 1 == len(db.Compras)
    def test_AddGameToInventory(self):
        id = db.index
        juego = Game(id,"Test",1,1,"Acción","PC",5)
        largoAntesCompras = len(db.Compras)
        addGameToInventory(id,juego)  
        largoAntes = len(db.Inventario)     
        # agrega de nuevo el juego, pero ahora solo debe actualizar las cantidades      
        addGameToInventory(id,juego)     
        #print("1. ",largoAntes,len(db.Inventario))  
        #print("2. ",largoAntesCompras + 1,len(db.Compras))
        #print("3. ",db.Inventario[id].count,10)
        assert largoAntes == len(db.Inventario) and largoAntesCompras + 2 == len(db.Compras) and db.Inventario[id].count == 10 
    # Probar: cantidad a vender < cantidad en inventario
    def test_Sale_1(self):
        id = db.index
        juego = Game(id,"Test_Sale_1",1,1,"Acción","PC",5)
        addGameToInventory(id,juego)   
        juego, valid, sms = validVenta("Test_Sale_1",4)
        assert True == valid
    # Probar: cantidad a vender = cantidad en inventario
    def test_Sale_2(self):
        id = db.index
        juego = Game(id,"Test_Sale_2",1,1,"Acción","PC",5)
        addGameToInventory(id,juego)   
        juego, valid, sms = validVenta("Test_Sale_2",5)
        assert True == valid
    # Probar: cantidad a vender > cantidad en inventario
    def test_Sale_3(self):
        id = db.index
        juego = Game(id,"Test_Sale_3",1,1,"Acción","PC",5)
        addGameToInventory(id,juego)   
        juego, valid, sms = validVenta(juego.DetailSale_Product(),6)
        assert valid == False and sms == "No hay stock suficiente"
    # Probar: cantidad a vender = 0
    def test_Sale_4(self):
        id = db.index
        juego = Game(id,"Test_Sale_4",1,1,"Acción","PC",1)
        addGameToInventory(id,juego)   
        juego, estado, sms = validVenta("Test_Sale_4",0)
        assert False == estado and sms == "Ingrese una cantidad mayor que 0"
    # Probar: cantidad a vender negativa
    def test_Sale_5(self):
        id = db.index
        juego = Game(id,"Test_Sale_5",1,1,"Acción","PC",0)
        addGameToInventory(id,juego)   
        juego, estado, sms = validVenta("Test_Sale_5",-1)
        assert False == estado and sms == "Ingrese una cantidad mayor que 0"
    # Probar que se genero el report
    def test_report(self):
        directorio = '.'  # Ruta al directorio actual
        nombre_archivo = db.reportTXT()    # Nombre del archivo de reporte
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        assert os.path.exists(ruta_archivo) == True
    

if __name__ == '__main__':
    unittest.main()