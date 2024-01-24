class HighVoltage:
    
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
        
        if self.prom > 220:
            return 1
        else:
            return 0
            
    
    def initApp(self):
        self.getVoltages(5)
        
        if self.logic():
            print (f"<ALTO VOLTAJE= {self.prom} V") 
        else:
            print (f"<VOLTAJE CORRECTO= {self.prom} V")
            

if __name__=='__main__':
    ejercicio1 = HighVoltage()
    
    ejercicio1.initApp() 
            
        
        
        
                   