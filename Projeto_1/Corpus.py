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
class Corpus(object):
    def __init__(self, diretorio):
        self.diretorio=diretorio
        self.lDocumentos = lde.ListaDupla()

    def carregarDiretorio(self):
        for arquivo in glob.glob(self.diretorio+'/*txt'):
            self.lDocumentos.anexar(self.carregarDoc(arquivo))

    def carregarDoc(self,arqv):
        lista = []
        nPalavras = 0
        for linha in open(arqv,'r'):
            palavra = ""
            for i in linha:
                cod = ord(i)
                if (cod >= 48 and cod<=57) or(cod >= 65 and cod<=90) or (cod >= 97 and cod<=122):
                    if (cod >= 65 and cod<=90):
                        palavra += chr(cod+32)
                    else:
                        palavra += i
                elif i.strip() == "" and palavra !="":
                    lista.append(palavra)
                    nPalavras +=1
                    palavra = ""
        documento = myDoc.Documento(lista,nPalavras)
        return documento


caminho =  "C:\\Users\\NTI\\Downloads\\dados\\src\\"
a = Corpus(caminho)
b = a.carregarDoc(caminho+"source-document00010.txt")
c = a.carregarDoc("C:\\Users\\NTI\\Downloads\\dados\\susp\\suspicious-document00005.txt")
b.contencao(c)


