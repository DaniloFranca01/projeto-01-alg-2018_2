'''
Created on 28 de set de 2018

@author: danilo
'''
from ListaDupla import Lista
from dataclasses import replace
class NGrama(Lista):
    '''
    classdocs
    '''
    def __init__(self):
        super().__init__(None)
        
    def __repr__(self):
        return "NGrama("+self.__str__()+")" 
    
    replace()