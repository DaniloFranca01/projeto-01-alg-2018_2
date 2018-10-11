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

import numpy as np
import ListaDupla as lde
import NGrama as ng
class Documento():

    def __init__(self,listaPalavras,nPalavras):
        self.__nPalavras = nPalavras
        self.__vPalavras = listaPalavras
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

    def __str__(self):
        return str(self.__vPalavras)

    def __repr__(self):
        return self.__str__()
    
    def contencao(self,documento):
        intersec = 0
        for x in documento.lNGrams:
            for y in self.lNGrams:
                if x == y: 
                    intersec += 1
        c = intersec/documento.nNgrams
        
    def gerarNGramas(self,n,lista):
        for i in range(0,self.nPalavras):
            if (i+n) > self.nPalavras:
                return lista
            palavras = ""
            for j in range(i,i+n):
                palavras+= self.__vPalavras[j]+","
            palavras = palavras.strip(",")
            palavras = palavras.split(",")
            nGram = ng.NGrama(palavras)
            lista.anexar(nGram)
            self.nNGrams+=1
            del(nGram)
        return lista