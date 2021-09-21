class moto():
    def __init__(self,name):
        self.nombre = name
    
    def arrancar(self):
        print("estoy arrancando ",self.nombre)
        
    def frenar(self):
        print("estoy frenado ",self.nombre)
        
rtx150 = moto("daniel")
duke200 = moto("brayan")

rtx150.arrancar()
duke200.frenar()