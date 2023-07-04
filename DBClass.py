from GameClass import Game
from datetime import datetime

class DataBase:
    def __init__(self):
        self.index = 0
        self.Inventario = dict()
        self.Plataformas = ["Consola","PC","Móvil"]
        self.Generos = ["Acción","Aventura","Arcade","Deportes","Estrategia","Simulación","Juegos de Mesa","Supervivencia"]
        self.Perfiles = ["Administrador","Cliente"]
        self.Compras = []
        self.Ventas = []
    
    def updateGame(self,key,value):
        self.DataBase[key] = value

    def addGame(self,game):
        self.DataBase[game.id] = game
    
    def updateIndex(self):
        self.index += 1


    def showInventory(self):
        for item in self.Inventario:
            print(self.Inventario[item].toString())

    def Save(self):
        file = open("DB_Inventario.txt","w")
        for item in self.Inventario:
            texto = str(self.Inventario[item].writeFile())
            if texto != "" and texto != "\n":
                file.write(texto)
        file.close()

        file = open("DB_Ventas.txt","w")
        for item in self.Ventas:
            texto = str(item.writeFile())
            if texto != "" and texto != "\n":
                file.write(texto)
        file.close()
        texto = []
        print("Compras",self.Compras)
        for item in self.Compras:
            texto.append(str(item.writeFile())+"\n")
        with open("DB_Compras.txt","w") as file:
            file.writelines(texto)

    def ReadFile(self):
        file = open("DB_Inventario.txt","r")
        for linea in file:
            id,title,platform,gender,priceBuy,priceSale,cant = linea.split(',')
            self.Inventario[id] = Game(id,title,priceBuy,priceSale,gender,platform,cant)
        file.close()

        file = open("DB_Ventas.txt","r")
        for linea in file:
            id,title,platform,gender,priceBuy,priceSale,cant = linea.split(',')
            self.Ventas.append(Game(id,title,priceBuy,priceSale,gender,platform,cant))
        file.close()

        file = open("DB_Compras.txt","r")
        for linea in file:
            id,title,platform,gender,priceBuy,priceSale,cant = linea.split(',')
            self.Compras.append(Game(id,title,priceBuy,priceSale,gender,platform,cant))
        file.close()

    def reportTXT(self):
        formatoNombre = "%d-%m-%Y %H.%M.%S"
        file = open("Reporte_"+str(datetime.now().strftime(formatoNombre))+".txt","w")
        formato = "%d/%m/%Y %H:%M:%S"
        file.write(f"Fecha: {datetime.now().strftime(formato)}\n\n")
        file.write("Reporte de Compras\n")
        file.write(f"=> Cantidad de Compras: {len(self.Compras)} compras realizadas.\n")
        cantJuegos = 0
        costo = 0
        detalle = ""
        for juego in self.Compras:
            cantJuegos += int(juego.count)
            costo += float(juego.priceBuy)*float(juego.count)
            detalle += juego.DetailBuy_toString()
        file.write(f"=> Cantidad de Juegos Comprados: {cantJuegos} juegos.\n")
        file.write(f"=> Costo total: $ {costo}.\n\n Detalle de Compra: \n"+detalle)

        file.write("Reporte de Ventas\n")
        cantJuegos = 0
        costo = 0
        detalle = ""
        for juego in self.Ventas:
            cantJuegos += int(juego.count)
            costo += float(juego.priceSale)*float(juego.count)
            detalle += juego.DetailSale_toString()
        file.write(f"=> Cantidad de Juegos Vendidos: {cantJuegos} juegos.\n")
        file.write(f"=> Venta total: $ {costo}.\n\n Detalle de la Venta: \n"+detalle)

        file.close()