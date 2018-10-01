import numpy as np
class Documento():
    
    def __init__(self,diretorio):
        self.diretorio=diretorio
        self.nPalavras = 0
        self.vPalavras = None
    
    def __str__(self):
        return str(self.vPalavras)
    
    def __repr__(self):
        return self.__str__()
    
    def carregarDoc(self):
        lista = []
        arq=open(self.diretorio,'r')
        arq=arq.read()
        palavra = ""
        for i in arq:
            cod = ord(i)
            if (cod >= 65 and cod<=90) or (cod >= 97 and cod<=122):
                palavra += i
            elif i == " " and palavra !="":
                lista.append(palavra)
                self.nPalavras +=1
                palavra = ""
        
        self.vPalavras = np.array(lista, dtype=object)
        
        
              
a = Documento("C:\\Users\danilo.DESKTOP-8QL5HFM\Downloads\Projeto 1 ALG\dados\src\source-document00010.txt")
a.carregarDoc()
print(str(a))   