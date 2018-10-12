import Corpus as c
import glob
import Documento as myDoc
class Teste(object):
    def __init__(self, diretorio):
        self.diretorio=diretorio

    def carregarDiretorio(self):
        caminho =  "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\src\\"
        corp = c.Corpus(caminho)
        corp.carregarDiretorio()
        for arquivo in glob.glob(self.diretorio + '/*txt'):
            doc = (self.carregarDoc(arquivo))
            corp.verificaPlagio(doc, 0.2)

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

csusp = "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\susp\\"
caminho =  "C:\\Users\\danilo.DESKTOP-8QL5HFM\\Downloads\\Projeto 1 ALG\\dados\\src\\"
corp = c.Corpus(caminho)
corp.carregarDiretorio()
teste = Teste(csusp)
doc = teste.carregarDoc(csusp+"suspicious-document00005.txt")
docsBasePlagio=corp.verificaPlagio(doc, 0.2)
#teste.carregarDiretorio()
print(len(docsBasePlagio))
