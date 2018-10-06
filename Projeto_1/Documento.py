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

    def __init__(self,diretorio):
        self.diretorio=diretorio
        self.nPalavras = 0
        self.vPalavras = None
        self.lNGrams = lde.ListaDupla()

    def __str__(self):
        return str(self.vPalavras)

    def __repr__(self):
        return self.__str__()

    def gerarNGramas(self,n):
        self.vPalavras
        for i in range(0,self.nPalavras):
            if (i+n) > self.nPalavras:
                return
            palavras = ""
            for j in range(i,i+n):
                palavras+= self.vPalavras[j]+","
            nGram = ng.NGrama(palavras)
            self.lNGrams.anexar(nGram)
            del(nGram)
        del(aux)

    def carregarDoc(self):
        lista = []
        arq = open(self.diretorio,'r')
        texto = arq.readlines()
        for linha in texto:
            palavra = ""
            for i in linha:
                cod = ord(i)
                if (cod >= 48 and cod<=57) or(cod >= 65 and cod<=90) or (cod >= 97 and cod<=122):
                    palavra += i
                elif i.strip() == "" and palavra !="":
                    lista.append(palavra)
                    self.nPalavras +=1
                    palavra = ""
        arq.close()
        self.vPalavras = np.array(lista)
        self.gerarNGramas(4)


caminho =  'C:\\Users\\NTI\Downloads\dados\dados\src\source-document00010.txt'
a = Documento(caminho)
a.carregarDoc()
print(str(a.lNGrams))
print(str(a.vPalavras))