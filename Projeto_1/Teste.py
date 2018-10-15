import Corpus as c
import Documento as myDoc
class Teste(object):
    def __init__(self, diretorio):
        self.__diretorio=diretorio

    @property
    def diretorio(self):
        return self.__diretorio

    @diretorio.setter
    def diretorio(self,diretorio):
        self.__diretorio = diretorio

    def carregarDoc(self, arqv):
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
        documento = myDoc.Documento(lista, nPalavras)
        return documento


    def teste11(self, nomeFonte,diretorioSusp):
        '''
         Testa um documento suspeito para um fonte cujo nome informado se encontra no diretorio da classe
        '''
        corp = c.Corpus(self.diretorio)
        docFonte = corp.carregarDoc(self.diretorio+nomeFonte)
        corp.lDocumentos.anexar(docFonte)
        doc = self.carregarDoc(diretorioSusp)
        docsBasePlagio=corp.verificaPlagio(doc, 0.01)
        return len(docsBasePlagio)

    def teste1N(self,diretorioSusp):
        '''
        Testa um documento suspeito para todos os fontes do diretorio da classe
        '''
        corp = c.Corpus(self.diretorio)
        corp.carregarDiretorio()
        doc = self.carregarDoc(diretorioSusp)
        docsBasePlagio=corp.verificaPlagio(doc, 0.01)
        return len(docsBasePlagio)


caminhoSrc =  "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\src\\"
nomeFonte = "source-document03229.txt"
dirSusp= "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\src\\source-document03229.txt"

teste = Teste(caminhoSrc)
print(teste.teste11(nomeFonte, dirSusp))
print(teste.teste1N(dirSusp))