class TriangleArea:
    #b*h/2
    def __init__(self):
        self.area = 0
    
    def getDataAndOperate(self): 
        base = float(input(f"ingrese la base: "))
        altura = float(input(f"ingrese la altura: "))
         
        self.area = base*altura/2
            

    
    def logic(self):
        if self.area > 1000:
            return 1
        else:
            return 0
            
    
    def initApp(self):
        self.getDataAndOperate()
        
        if self.logic():
            print (f"<DATOS NO VALIDOS= {self.area}>") 
        else:
            print (f"<EL AREA ES= {self.area}>")
            

if __name__=='__main__':
    ejercicio1 = TriangleArea()
    
    ejercicio1.initApp() 
            
        
        
        
                   