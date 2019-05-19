'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2018-09-28

Descricao:  Lista duplamente encadeada.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Danilo Leite de Franca
'''

class _No:

    def __init__(self, item=None, ant=None, prox=None):
        self.item = item
        self.prox = prox
        self.ant = ant


class ListaDupla(object):
    '''
    Lista Duplamente Encadeada
    '''
    class Iterador:
        def __init__(self, primeiro):
            self.atual = primeiro

        def __next__(self):
            if self.atual == None:
                raise StopIteration
            item = self.atual.item
            self.atual = self.atual.prox
            return item

    def __init__(self,objUniv = None):
        self.__objUniv = objUniv
        self.__primeiro = self.__ultimo = _No()
        self.tamanho = 0
        if self.__objUniv != None:
            self.estender(objUniv)
        del(self.__objUniv)

    @property
    def objUniv(self):
        return self.__objUniv

    @objUniv.setter
    def objUniv(self, objUniv):

        self.__objUniv = objUniv

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
        return "{0}".format(self.__class__.__name__)+self.__str__()+")"

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
        ref = self.__primeiro.prox
        if (indice > (self.tamanho-1)) or (indice < 0):
            return IndexError
        for x in range(self.tamanho):
            if x != indice:
                ref = ref.prox
            else:
                return ref.item

    def __setitem__(self, indice,valor):
        ref = self.__primeiro.prox
        if (indice > (self.tamanho-1)) or (indice < 0):
            return IndexError
        for x in range(self.tamanho):
            if x != indice:
                ref = ref.prox
            else:
                ref.item = valor

    def vazia(self):
        '''
        Verifica se a lista esta vazia
        '''
        return self.__primeiro == self.__ultimo

    def estender(self,iteravel):
        '''
        Recebe um objeto iteravel como parametro e retorna a lista estendida com o objeto informado
        '''
        for x in iteravel:
            self.anexar(x)

        return self

    def copiar(self):
        '''
        Retorna a copia exata da lista
        '''
        saida = ListaDupla()
        aux = self.__primeiro.prox
        while aux.prox != None:
            saida.anexar(aux.item)
            aux= aux.prox
        saida.anexar(aux.item)
        return saida

    def pesquisar(self, item):
        '''
        Recebe como parametro um item e retorna se for encontrado
        '''
        aux = self.__primeiro.prox
        while not aux is None and aux.item != item:
            aux = aux.prox
        if aux is None:
            raise ValueError
        return aux.item

    def anexar(self, item):
        '''
        Recebe como parametro um item e adiciona no final da lista
        '''
        self.__ultimo.prox = _No(item, self.__ultimo,None)
        self.__ultimo = self.__ultimo.prox
        self.tamanho +=1

    def inserirInicio(self, item):
        '''
        Recebe como parametro um item e adiciona no inicio da lista
        '''
        aux = _No(item, self.__primeiro, self.__primeiro.prox)
        self.__primeiro.prox = aux
        if self.vazia():
            self.__ultimo = aux
        else:
            aux.prox.ant = aux
        self.tamanho +=1

    def inserirOrdenado(self, item):
        '''
        Recebe como parametro um item e adiciona de forma ordenada na lista
        '''
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
        '''
        Remove a primeira posicao da lista
        '''
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
        '''
        Remove a ultima posicao da lista
        '''
        if(self.vazia()): return None
        aux = self.__ultimo
        self.__ultimo = aux.ant
        self.__ultimo.prox = None
        item = aux.item
        aux.prox = aux.ant = None
        del aux
        self.tamanho -=1
        return item
