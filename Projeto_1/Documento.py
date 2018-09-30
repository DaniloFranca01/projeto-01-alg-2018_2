class Documento():
    
    def __init__(self,diretorio):
        self.lista= []
        self.diretorio=diretorio
    
    def __str__(self):
        return str(self.lista)
    
    def __repr__(self):
        return self.__str__()
    
    def carregarDoc(self):
        specChars = ("\n",":",".","<",">","(",")","/",'"',",")
        arq=open(self.diretorio,'r')
        arq=arq.read()
        palavra = ""
        for i in arq:
            if (not i in specChars) and (i != " "):
                palavra += i
            elif i == " ":
                self.lista.append(palavra)
                palavra = "" 
                
              
a = Documento("C:\\Users\danilo.DESKTOP-8QL5HFM\Downloads\Projeto 1 ALG\dados\src\source-document00010.txt")
a.carregarDoc()
print(str(a))   