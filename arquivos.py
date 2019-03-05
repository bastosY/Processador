

from Decodificador import *
from Unidade_de_Controle import *
from Memoria import *
from Ula import *

unidade = Unidade_de_Controle()
arquivo = open("/home/tyn/Projetos/Python/Processador/newFile.txt", "w")

while True:
    try:
        arquivo.write(str(bin(unidade.getInstrucoes(unidade.getPC()))[2:])+"\n")
        unidade.controle(unidade.getInstrucoes(unidade.getPC()))
        unidade.setPC()
    except IndexError:
        print("limite")
        break


arquivo.close()