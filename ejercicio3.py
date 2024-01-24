class Voltage:
    
    def __init__(self):
        self.voltageList = []
        self.prom = 0
    
    def getVoltages(self, voltsN): 
        
        for i in range(voltsN):
            data = float(input(f"ingrese el voltaje {i+1}: ")) 
            self.voltageList.append(data)
            
    def calculateProm(self):
        return sum(self.voltageList)/len(self.voltageList)
    
    def logic(self):
        
        self.prom = self.calculateProm()
        
        if self.prom < 115:
            print (f"<VOLTAJE CORRECTO= {self.prom} V")
        elif  self.prom > 115 and self.prom < 220:
            print (f"<ALTO VOLTAJE= {self.prom} V") 
        else:
            print (f"<PELIGRO= {self.prom} V")

            
    
    def initApp(self):
        self.getVoltages(3)
        self.logic()

           
            

if __name__=='__main__':
    ejercicio1 = Voltage()
    
    ejercicio1.initApp() 
            
        
        
        