import numpy as np
import ListaDupla as lde
import NGrama as ng
class Documento():
    
    def __init__(self,diretorio):
        self.diretorio=diretorio
        self.nPalavras = 0
        self.vPalavras = None
        self.lNGrams = lde.Lista() 
    
    def __str__(self):
        return str(self.vPalavras)
    
    def __repr__(self):
        return self.__str__()
            
    def gerarNGramas(self,n):
        aux = self.vPalavras
        for i in range(0,self.nPalavras):
            if (i+n) > self.nPalavras:
                return
            nGram = ng.NGrama() 
            for j in range(i,i+n):
                nGram.anexar(aux[j])
            self.lNGrams.anexar(nGram)
            del(nGram)
        del(aux)        
        
    def carregarDoc(self):
        lista = []
        arq=open(self.diretorio,'r')
        arq=arq.read()
        palavra = ""
        for i in arq:
            cod = ord(i)
            if (cod >= 48 and cod<=57) or(cod >= 65 and cod<=90) or (cod >= 97 and cod<=122):
                palavra += i
            elif i.strip() == "" and palavra !="":
                lista.append(palavra)
                self.nPalavras +=1
                palavra = ""
        
        self.vPalavras = np.array(lista)
        self.gerarNGramas(3)     
            
        
              
a = Documento("C:\\Users\danilo.DESKTOP-8QL5HFM\Downloads\Projeto 1 ALG\dados\src\source-document00010.txt")
a.carregarDoc()
print(str(a.lNGrams))
print(str(a.vPalavras))   