class MtoKM:
    #b*h/2
    def __init__(self):
        self.kM = 0
        self.m = 0
    
    def getDataAndOperate(self): 
        self.m = float(input(f"ingrese la ditancia en m: "))
         
        self.kM = self.m*(1.0/1000)
            
    
    def initApp(self):
        self.getDataAndOperate()
        
        
        print (f" <{self.m} m son {self.kM} km>") 
            

if __name__=='__main__':
    ejercicio1 = MtoKM()
    
    ejercicio1.initApp() 
            