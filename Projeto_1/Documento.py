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
        self.nPalavras = nPalavras
        self.__vPalavras = listaPalavras
        self.__lNGrams =  self.gerarNGramas(3,lde.ListaDupla())

    @property
    def vPalavras(self):
        return self.__vPalavras

    @vPalavras.setter
    def vPalavras(self, lista):
        self.__vPalavras = np.array(lista)

    @property
    def lNGrams(self):
        return self.__lNGrams

    @lNGrams.setter
    def lNGrams(self, lista):
        self.__lNGrams = lista


    def __str__(self):
        return str(self.__vPalavras)

    def __repr__(self):
        return self.__str__()

    def gerarNGramas(self,n,lista):
        for i in range(0,self.nPalavras):
            if (i+n) > self.nPalavras:
                return lista
            palavras = ""
            for j in range(i,i+n):
                palavras+= self.__vPalavras[j]+","
            palavras.strip(",")
            nGram = ng.NGrama(palavras.split(","))
            lista.anexar(nGram)
            del(nGram)
        return lista