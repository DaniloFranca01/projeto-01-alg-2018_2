'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2018-09-28

Descricao:  Classe NGrama.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Danilo Leite de Franca
'''

class NGrama():
    '''
    Representacao de um N-Grama com tamanho variavel
    '''
    def __init__(self, docRef,inicio,fim):
        self.__docRef = docRef
        self.__inicio = inicio
        self.__fim = fim

    @property
    def docRef(self):
        return self.__docRef

    @docRef.setter
    def docRef(self, docRef):
        self.__docRef = docRef

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    def __rpr__(self):
        return "NGrama({0}, {1}, {2})".format(self.__docRef.__repr__(), self.__inicio, self.__fim)

    def __str__(self):
        return " ".join(self.__docRef.vPalavras[n] for n in range (self.__inicio, self.__fim+1))
