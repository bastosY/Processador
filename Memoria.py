from Decodificador import *
 
class Memoria(object):

    __instrucoes = [2281702741, 2218186752, 469762048, 67108864]
    __reg1 = 0
    __reg2 = 0
    __pc = 0
    __memoriaArmazenada = list()


    def setInstrucoes(self, posicao, dado):
        self.__instrucoes[posicao] = dado

    def getInstrucoes(self, posicao):
        return self.__instrucoes[posicao]

    def setReg1(self, dado):
        self.__reg1 = dado

    def getReg1(self):
        return self.__reg1

    def setReg2(self, dado):
        self.__reg2 = dado

    def getReg2(self):
        return self.__reg2

    def setPC(self):
        self.__pc += 1
    
    def getPC(self):
        return self.__pc

    def setMemoriaArmazenada(self, dado):
        self.__memoriaArmazenada.append(dado)

    def getMemoriaArmazenada(self, posicao):
        return self.__memoriaArmazenada[posicao]


