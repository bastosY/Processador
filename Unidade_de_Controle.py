from Decodificador import *
from Memoria import *
from Ula import *

class Unidade_de_Controle(Memoria, Decodificador, Ula):
    
    
    def controle(self, word):
        self._conversor(word)
        self.__verificarOpcode()
        self.__verificarTamanhoReg()

    
    def halt(self):
        input("")

    def mov(self, Reg1, Reg2, dado):
        if(Reg1 == "reg1"):
            self.setReg1(dado)

        elif(Reg2 == "reg2"):
            self.setReg2(dado)
        
        else: 
            self.setReg1(self.getReg2())
        
    #Verifica qual instrução será executada
    def __verificarOpcode(self):

        Memoria.__init__(self)

        #VR possui o valor 00
        if(self.getVerificador_2bits() == 0):
            print("Error:101")

        #VR possui o valor 01
        elif(self.getVerificador_2bits() == 1):

            #Realiza o halt
            if(self.getOpcode_4bits() == 0):
                self.halt()
            
            #Realiza a soma entre um registrador e um dado 
            elif(self.getOpcode_4bits() == 1): 
                self.setReg2(self.soma(self.getReg2(), self.getReg1_11bits()))
                self.setMemoriaArmazenada(self.getReg2())

            #Realiza a subtração entre um registrador e um dado
            elif(self.getOpcode_4bits() == 2): 
                self.setReg2(self.subtracao(self.getReg2(), self.getReg1_11bits()))
                self.setMemoriaArmazenada(self.getReg2())

            #Realiza a multiplicação entre um registrador e um dado
            elif(self.getOpcode_4bits() == 3): 
                self.setReg2(self.multiplicacao(self.getReg2(), self.getReg1_11bits()))
                self.setMemoriaArmazenada(self.getReg2())

            #Realiza o "e" lógico entre um registrador e um dado
            elif(self.getOpcode_4bits() == 4): 
                self.setReg2(self.and_logico(self.getReg2(), self.getReg1_11bits))
                self.setMemoriaArmazenada(self.getReg2())

            #Realiza o "ou" lógico entre um registrador e um dado
            elif(self.getOpcode_4bits() == 5): 
                self.setReg2(self.or_logico(self.getReg2(), self.getReg1_11bits()))
                self.setMemoriaArmazenada(self.getReg2())

            elif(self.getOpcode_4bits() == 6): #Jump on negative
                pass
            elif(self.getOpcode_4bits() == 7): #Jump incondicional
                pass

            #Movimenta os dados para o reg2
            elif(self.getOpcode_4bits() == 8): 
                self.mov("Null", "reg2", self.getReg1_11bits())


        #VR possui o valor 10
        elif(self.getVerificador_2bits() == 2):

            #Realiza o halt
            if(self.getOpcode_4bits() == 0):
                self.halt()
            
            #Realiza a soma entre um registrador e um dado 
            elif(self.getOpcode_4bits() == 1): 
                self.setReg1(self.soma(self.getReg1(), self.getReg2_11bits()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza a subtração entre um registrador e um dado
            elif(self.getOpcode_4bits() == 2): 
                self.setReg1(self.subtracao(self.getReg1(), self.getReg2_11bits()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza a multiplicação entre um registrador e um dado
            elif(self.getOpcode_4bits() == 3): 
                self.setReg1(self.multiplicacao(self.getReg1(), self.getReg2_11bits()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza o "e" lógico entre um registrador e um dado
            elif(self.getOpcode_4bits() == 4): 
                self.setReg1(self.and_logico(self.getReg1(), self.getReg2_11bits))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza o "ou" lógico entre um registrador e um dado
            elif(self.getOpcode_4bits() == 5): 
                self.setReg1(self.or_logico(self.getReg1(), self.getReg2_11bits()))
                self.setMemoriaArmazenada(self.getReg1())

            elif(self.getOpcode_4bits() == 6): #Jump on negative
                pass
            elif(self.getOpcode_4bits() == 7): #Jump incondicional
                pass
            
            #Movimenta os dados para o reg1
            elif(self.getOpcode_4bits() == 8): 
                self.mov("reg1", "Null", self.getReg2_11bits())

        #VR possui o valor 11
        elif(self.getVerificador_2bits() == 3):

            #Reliza o halt
            if(self.getOpcode_4bits() == 0): 
                self.halt()

            #Realiza a soma entre 2 registradores
            elif(self.getOpcode_4bits() == 1): 
                self.setReg1(self.soma(self.getReg1(), self.getReg2()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza a subtração entre 2 registradores
            elif(self.getOpcode_4bits() == 2):
                self.setReg1(self.subtracao(self.getReg1(), self.getReg2()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza a multiplicação entre 2 registradores
            elif(self.getOpcode_4bits() == 3): 
                self.setReg1(self.multiplicacao(self.getReg1(), self.getReg2()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza o "e" lógico entre 2 registradores
            elif(self.getOpcode_4bits() == 4):
                self.setReg1(self.and_logico(self.getReg1(), self.getReg2()))
                self.setMemoriaArmazenada(self.getReg1())

            #Realiza o "ou" lógico entre 2 registradores
            elif(self.getOpcode_4bits() == 5): 
                self.setReg1(self.or_logico(self.getReg1(), self.getReg2()))
                self.setMemoriaArmazenada(self.getReg1())

            elif(self.getOpcode_4bits() == 6): #Jump on negative
                pass
            elif(self.getOpcode_4bits() == 7): #Jump incondicional
                pass
            elif(self.getOpcode_4bits() == 8): #Mov
                self.mov("Null", "Null", "Null")
        
    #Faz a flag do tamanho do registrador
    def __verificarTamanhoReg(self):
        if(self.getTamanho_4bits() == 0):
            pass
        elif(self.getOpcode_4bits() == 1):
            pass
        elif(self.getOpcode_4bits() == 2):
            pass
        elif(self.getOpcode_4bits() == 3):
            pass
        elif(self.getOpcode_4bits() == 4):
            pass
        elif(self.getOpcode_4bits() == 5):
            pass
        elif(self.getOpcode_4bits() == 6):
            pass


#x = Unidade_de_Controle()
#x.controle(2344617983)
#print(x.getReg1())
