'''
Created on 31 de out de 2018

@author: dlf3
'''
import numpy as np
from numpy import object
import ListaDupla as lde
class No(object):

    def __init__(self, caracter = None, documentos = None):
        self.caracter = caracter
        self.documentos = lde.ListaDupla()
        self.filhos = np.ndarray(shape=37, dtype=object)

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.caracter, self.documentos)

class Trie(object):
    '''
    Representacao de uma arvore trie
    '''
    def __init__(self):
        self.raiz = No()

    def __getitem__(self, item):
        return self.raiz.pesquisar(item)

    def __repr__(self):
        return self.raiz.__repr__()

    def __str__(self):
        info = []
        self.__texto(palavras = info)
        texto = ""
        for dupla in info:
            if texto:
                texto += ", "
            texto += '"{}"({})'.format(dupla[0], dupla[1])
        return texto

    def char(self, num):
        if num >= 0 and num <= 25:
            return chr(num + ord('a'))
        elif num >= 26 and num <= 35:
            return chr(num+ord('0')-26)
        else:
            return ' '

    def texto(self, atual = "", palavras = []):
        for i in range(53):
            if not self.letras[i] is None:
                if self.letras[i].cont > 0:
                    palavras.append((atual+self.__char(i), self.letras[i].cont))
                    self.letras[i].__texto(atual+self.__char(i), palavras)

    @staticmethod
    def pos(char):
        if char >= 'a' and char <= 'z':
            return ord(char) - ord('a')
        elif char >= '0' and char <= '9':
            return ord(char) - ord('0') + 26
        else:
            return 36

    def inserir(self, ngrama):
        chave = str(ngrama)
        atual = self.raiz
        for c in chave:
            p = self.pos(c)
            if atual.filhos[p] is None:
                atual.filhos[p] = No(c)
            atual = atual.filhos[p]
        if atual.documentos is None:
            atual.documentos = []
        atual.documentos.anexar(ngrama.docRef)

    def pesquisar(self, ngrama):
        chave = str(ngrama)
        atual = self.raiz
        for c in chave:
            p = self.pos(c)
            if atual.filhos[p] is None:
                raise KeyError
            else:
                atual = atual.filhos[p]
        if atual.documentos is None:
            raise KeyError
        else:
            return atual.documentos


