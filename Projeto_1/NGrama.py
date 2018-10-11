'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2018-09-28

Descricao:  Classe NGrama herdada de uma Lista duplamente Encadeada.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Danilo Leite de Franca
'''

from ListaDupla import ListaDupla
class NGrama(ListaDupla):
    '''
    classdocs
    '''
    def __init__(self, palavras):
        super().__init__(palavras)
        
    def __eq__(self, ngrama):
        cont = 0 
        qtdTrue = 0
        for x in ngrama:
            if x == self[cont]:
                qtdTrue+= 1
            cont+= 1
        if self.tamanho == qtdTrue:
            return True
        else:
            return False
