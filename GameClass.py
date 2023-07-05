class Game:
    def __init__(self,id,title,priceBuy,priceSale,gender, platform,count):
        self.id = id
        self.title = title
        self.priceBuy = priceBuy
        self.priceSale = priceSale
        self.gender = gender
        self.platform = platform
        self.count = count
    
    def __repr__(self):
        return f"Producto:\n=> id: {self.id}\n=> title: {self.title}\n=> price buy/sale: {self.priceBuy}/{self.priceSale}\n=> platform: {self.platform}\n=> count: {self.count}"
    
    def toString(self):
        return f"Juego {self.id}: \n=> Título: {self.title}, Plataform: {self.platform}, Género: {self.gender}, Precio Compra: {self.priceBuy}, Precio Venta: {self.priceSale}, Cantidad Disponible: {self.count}"
    
    def DetailBuy_toString(self):
        return f"=> Título: {self.title}, Plataform: {self.platform}, Género: {self.gender}, Precio Compra: {self.priceBuy}, Cantidad: {self.count}\n"
    
    def DetailSale_toString(self):
        return f"=> Título: {self.title}, Plataform: {self.platform}, Género: {self.gender}, Precio Venta: {self.priceSale}, Cantidad: {self.count}\n"
    
    def DetailSale_Product(self):
        return f"Título: {self.title}, Plataform: {self.platform}, Género: {self.gender}, Precio Venta: {self.priceSale}, Cantidad: {self.count}"
    
    def writeFile(self):
        return f"{self.id},{self.title},{self.platform},{self.gender},{self.priceBuy},{self.priceSale},{self.count}"