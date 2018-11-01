'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2018-09-28

Descricao:  Classe Corpus.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Danilo Leite de Franca
'''

import glob
import ListaDupla as lde
import Documento as myDoc
import os
from Trie import Trie
class Corpus(object):
    '''
    Representacao de um conjunto de documentos
    '''
    def __init__(self, diretorio):
        self.__diretorio=diretorio
        self.lDocumentos = lde.ListaDupla()
        self.trieDocs = Trie()

    @property
    def diretorio(self):
        return self.__diretorio

    @diretorio.setter
    def diretorio(self, diretorio):
        self.__diretorio = diretorio


    def carregarDiretorio(self):
        '''
        Carrega todos os arquivos no deretorio Informado
        '''
        for arquivo in glob.glob(self.__diretorio+'/*txt'):
            nomeArquivo = os.path.basename(arquivo)
            self.gerarTrie(self.carregarDoc(arquivo,nomeArquivo))

    def carregarDoc(self,arqv,nomeArqv):
        '''
        Carrega um documento no deretorio Informado
        '''
        lista = []
        nPalavras = 0
        for linha in open(arqv,'r',encoding="utf8"):
            palavra = ""
            linhaLen = len(linha)
            contChar = 0
            for i in linha:
                contChar+=1
                cod = ord(i)
                if (cod >= 48 and cod<=57) or(cod >= 65 and cod<=90) or (cod >= 97 and cod<=122):
                    if (cod >= 65 and cod<=90):
                        palavra += chr(cod+32)
                    else:
                        palavra += i
                elif ((i.strip() == "") or(linhaLen == contChar)) and palavra !="":
                    lista.append(palavra)
                    nPalavras +=1
                    palavra = ""
        documento = myDoc.Documento(lista,nPalavras,nomeArqv)
        return documento

    def gerarTrie(self,doc):
        for ngrama in doc.lNGrams:
            self.trieDocs.inserir(ngrama)


    def verificaPlagio(self,documento,limiar):
        '''
        Recebe como parametro um documento e um limiar
        retorna uma lista de documentos prováveis
        que serviram de base para o documento informado
        '''
        lDocBases = lde.ListaDupla()
        for x in self.lDocumentos:
            contencao = x.contencao(documento)
            if contencao > limiar:
                lDocBases.inserirOrdenado(x)
        return lDocBases


