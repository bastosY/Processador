from Decodificador import *
from Unidade_de_Controle import *
from Memoria import *
from Ula import *

unidade = Unidade_de_Controle()



while True:
    try:
        unidade.controle(unidade.getInstrucoes(unidade.getPC()))
        if(unidade.getPC() == 0):
            print(unidade.getReg1())
        elif(unidade.getPC() == 1):
            print(unidade.getReg2())
        elif(unidade.getPC() == 2):
            print(unidade.getReg1())
        unidade.setPC()
    except IndexError:
        print("limite")
        break