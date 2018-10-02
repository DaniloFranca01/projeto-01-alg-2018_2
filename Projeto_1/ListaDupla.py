class _No:

    def __init__(self, item=None, ant=None, prox=None):
        self.item = item
        self.prox = prox
        self.ant = ant
    
   
class Lista(object):
    
    class Iterador: 
        def __init__(self):
            self.__atual = self.__primeiro.prox
                
        def __next__(self):
            if self.atual == None:
                raise StopIteration
            item = self.atual.item
            self.atual = self.atual.prox
            return item 
    
    def __init__(self,objUniv = None):
        self.objUniv = objUniv
        self.__primeiro = self.__ultimo = _No()
        self.tamanho = 0
        if self.objUniv != None:
            self.estender(objUniv)
        del(self.objUniv)
        
        
    def __str__(self):
        aux = self.__primeiro.prox
        saida = "["
        while aux is not None:
            saida += str(aux.item)+","
            aux = aux.prox
        saida = saida.strip(",")
        saida +="]"
        return saida
    
    def __repr__(self):
        return "ListaDupla("+self.__str__()+")" 
    
    def __len__(self):
        return self.tamanho  
        
    def __iter__(self):
        return self.Iterador(self.__primeiro.prox)
    
    def __contains__(self,arg):
        if self.__primeiro == None:
            return False
        else:
            aux = self.__primeiro
            while aux.prox is not None:
                if aux.item == arg:
                    return True
                aux = aux.prox
            return False
            
    def __getitem__(self, indice):
        return self.percorrerIndice(indice)
            
    def __setitem__(self, indice,valor):
        ref = self.percorrerIndice(indice)
        ref = valor
         
                
    def percorrerIndice(self,indice):             
        ref = self.__primeiro.prox
        if (indice > (self.tamanho-1)) or (indice < 0):
            return IndexError
        for x in range(self.tamanho):
            if x != indice:
                ref = ref.prox
            else:
                return ref.item 
    

    def vazia(self):
        return self.__primeiro == self.__ultimo
    
    def estender(self,iteravel):
        for x in iteravel:
            self.anexar(x)
                
        return self
    
    def copiar(self):
        saida = Lista()
        aux = self.__primeiro.prox
        while aux.prox != None:
            saida.anexar(aux.item)
            aux= aux.prox
        saida.anexar(aux.item)
        return saida
       
    def pesquisar(self, item):      
        aux = self.__primeiro.prox
        while not aux is None and aux.item != item:
            aux = aux.prox
        if aux is None:
            raise ValueError    
        return aux.item
    
    def anexar(self, item):
        self.__ultimo.prox = _No(item, self.__ultimo,None)
        self.__ultimo = self.__ultimo.prox
        self.tamanho +=1 
    
    def inserirInicio(self, item):
        aux = _No(item, self.__primeiro, self.__primeiro.prox)
        self.__primeiro.prox = aux        
        if self.vazia():
            self.__ultimo = aux
        else:
            aux.prox.ant = aux 
        self.tamanho +=1    
    
    def inserirOrdenado(self, item):
        if self.vazia(): 
            self.anexar(item)
            return
        ref = self.__primeiro
        while not ref.prox is None and ref.prox.item <= item:
            ref = ref.prox
        aux = _No(item, ref,ref.prox)
        ref.prox = aux
        if aux.prox is None:
            self.__ultimo = aux
        else:
            aux.prox.ant = aux
        self.tamanho +=1 
            
    
    def removerInicio(self):
        if(self.vazia()): return None
        aux = self.__primeiro.prox
        self.__primeiro.prox = aux.prox        
        item = aux.item
        if self.__ultimo == aux: 
            self.__ultimo = self.__primeiro
        else:
            aux.prox.ant = self.__primeiro
        aux.prox = None
        del aux
        self.tamanho -=1 
        return item

    def removerFim(self):
        if(self.vazia()): return None
        aux = self.__ultimo
        self.__ultimo = aux.ant
        self.__ultimo.prox = None
        item = aux.item
        aux.prox = aux.ant = None
        del aux
        self.tamanho -=1 
        return item
    
    def limpar(self):
        while self.__primeiro is not None:
            aux = self.__primeiro
            self.__primeiro = self.__primeiro.prox 
            aux.ant = aux.prox = None
            aux.item = None
            del(aux)
        self.__primeiro = self.__ultimo
        self.tamanho = 0

    