import Corpus as c
import Documento as myDoc
from Profile import time_Profile
from os import walk

class Teste(object):
    def __init__(self, diretorio):
        self.__diretorio=diretorio

    @property
    def diretorio(self):
        return self.__diretorio

    @diretorio.setter
    def diretorio(self,diretorio):
        self.__diretorio = diretorio

    def buscarArquivo(self,direct,nomeArquivo):
        '''
        Carrega todos os arquivos no deretorio Informado

        '''
        for (dirpath, dirnames,filenames) in walk(direct):
            if nomeArquivo in filenames:
                return self.carregarDoc(dirpath+nomeArquivo,nomeArquivo)

    def carregarDoc(self, arqv, nomeArqv):
        lista = []
        nPalavras = 0
        for linha in open(arqv, 'r',encoding="utf8"):
            palavra = ""
            for i in linha:
                cod = ord(i)
                if (cod >= 48 and cod <= 57) or(cod >= 65 and cod <= 90) or (cod >= 97 and cod <= 122):
                    if (cod >= 65 and cod <= 90):
                        palavra += chr(cod + 32)
                    else:
                        palavra += i
                elif i.strip() == "" and palavra != "":
                    lista.append(palavra)
                    nPalavras += 1
                    palavra = ""
        documento = myDoc.Documento(lista, nPalavras, nomeArqv)
        return documento

    @time_Profile
    def teste11(self,diretorioSusp,nomeSusp,nomeFonte):
        '''
         Testa um documento suspeito para um fonte cujo nome informado se encontra no diretorio da classe
        '''
        corp = c.Corpus(self.diretorio)
        docFonte = corp.carregarDoc(self.diretorio+nomeFonte,nomeSusp)
        corp.lDocumentos.anexar(docFonte)
        doc = self.carregarDoc(diretorioSusp+nomeSusp,nomeSusp)
        docsBasePlagio=corp.verificaPlagio(doc, 0.01)
        return self.salvarLogSaida(docsBasePlagio,nomeSusp)

    @time_Profile
    def teste1N(self,diretorioSusp,nomeSusp):
        '''
        Testa um documento suspeito para todos os fontes do diretorio da classe
        '''
        corp = c.Corpus(self.diretorio)
        corp.carregarDiretorio()
        doc = self.buscarArquivo(diretorioSusp,nomeSusp)
        docsBasePlagio=corp.verificaPlagio(doc, 0.01)
        return self.salvarLogSaida(docsBasePlagio,nomeSusp)

    def salvarLogSaida(self,listaDocs,nomeSusp):
        '''
        Salva o log da saida do teste
        '''
        saida=open('saida.txt', 'w')
        saida.write("Documento suspeito: "+nomeSusp+'\n')
        saida.write("Total de documentos que posivelmente serviram de base: "+str(len(listaDocs))+'\n')
        saida.write("NOME:CONTENÇÃO"+'\n')
        for docmt in listaDocs:
            saida.write(docmt.nomeDocumento+": "+str(docmt.contenVal)+'\n')
        saida.close()

caminhoSrc =  "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\src\\"
nomeFonte = "source-document03229.txt"

dirSusp= "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\susp\\"
nomeSusp = "suspicious-document00005.txt"

teste = Teste(caminhoSrc)
teste.teste1N(dirSusp,nomeSusp)
#teste.teste11(dirSusp,nomeSusp,nomeFonte)
print("Log Salvo na pasta")
