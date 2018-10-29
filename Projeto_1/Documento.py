'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2018-09-28

Descricao:  Classe Documento.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Danilo Leite de Franca
'''
from memory_profiler import profile
import numpy as np
import ListaDupla as lde
import NGrama as ng
class Documento():
    '''
    Representacao de um documento de texto
    '''
    def __init__(self,listaPalavras,nPalavras,nomeDocumento):
        self.__nPalavras = nPalavras
        self.__vPalavras = listaPalavras
        self.__nomeDocumento = nomeDocumento
        self.contenVal = 0
        self.nNGrams = 0
        self.lNGrams =  self.gerarNGramas(3,lde.ListaDupla())

    @property
    def vPalavras(self):
        return self.__vPalavras

    @vPalavras.setter
    def vPalavras(self, listaPalavras):
        self.__vPalavras = np.array(listaPalavras)

    @property
    def nPalavras(self):
        return self.__nPalavras

    @nPalavras.setter
    def nPalavras(self, nPalavras):
        self.__nPalavras = nPalavras

    @property
    def nomeDocumento(self):
        return self.__nomeDocumento

    @nomeDocumento.setter
    def nomeDocumento(self, nomeDocumento):
        self.__nomeDocumento = nomeDocumento

    def __str__(self):
        return str(self.__vPalavras)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.__nomeDocumento < other.__nomeDocumento:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__nomeDocumento <= other.__nomeDocumento:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__nomeDocumento == other.__nomeDocumento:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__nomeDocumento != other.__nomeDocumento:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__nomeDocumento > other.__nomeDocumento:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__nomeDocumento >= other.__nomeDocumento:
            return True
        else:
            return False

    '''
    Manutenção em andamento
    '''
    def contencao(self,documento):
        '''
        Recebe como parametro um documento e retorna a contencao do documento informado para cada documento em um diretorio
        '''
        intersec = 0
        for x in documento.lNGrams:
            for y in self.lNGrams:
                if x == y:
                    intersec += 1
        self.contenVal = intersec/documento.nNGrams
        return self.contenVal

    @profile
    def gerarNGramas(self,n,lista):
        '''
        Recebe como parametro uma lista e um valor N e retorna uma lista de N-gramas com o tamanho informado
        '''
        self.nNGrams = (self.nPalavras-n) +1
        for i in range(0,self.nNGrams):
            inicio = i
            fim = (i + n)-1
            ref = self
            nGram = ng.NGrama(ref,inicio,fim)
            lista.anexar(nGram)
            del(nGram)
        return lista
