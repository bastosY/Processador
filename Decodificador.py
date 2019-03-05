class Decodificador(object):

    def __init__ (self):
        self.__opcode_4bits = None
        self.__verificador_2bits = None
        self.__tamanho_4bits = None
        self.__reg1_11bits = None
        self.__reg2_11bits = None
        

    def setOpcode_4bits(self, opcode_4bits):
        self.__opcode_4bits = opcode_4bits

    def getOpcode_4bits(self):
        return self.__opcode_4bits

    def setVerificador_2bits(self, verificador_2bits):
        self.__verificador_2bits = verificador_2bits

    def getVerificador_2bits(self):
        return self.__verificador_2bits

    def setTamanho_4bits(self, tamanho_4bits):
        self.__tamanho_4bits = tamanho_4bits

    def getTamanho_4bits(self):
        return self.__tamanho_4bits

    def setReg1_11bits(self, reg1_11bits):
        self.__reg1_11bits = reg1_11bits

    def getReg1_11bits(self):
        return self.__reg1_11bits

    def setReg2_11bits(self, reg2_11bits):
        self.__reg2_11bits = reg2_11bits

    def getReg2_11bits(self):
        return self.__reg2_11bits   

    def _conversor(self, numb):

        opcode_4bits_aux = 4026531840
        verificador_2bits_aux = 201326592
        tamanho_4bits_aux = 62914560
        reg1_11bits_aux = 4192256
        reg2_11bits_aux = 2047


        #Identifica o opcode
        self.__opcode_4bits = numb & opcode_4bits_aux
        self.__opcode_4bits = self.__opcode_4bits >> 28
        

        #Verifica se são registradores
        self.__verificador_2bits = numb & verificador_2bits_aux
        self.__verificador_2bits = self.__verificador_2bits >> 26


        #Verifica o tamanho do registrador
        self.__tamanho_4bits = numb & tamanho_4bits_aux
        self.__tamanho_4bits = self.__tamanho_4bits >> 22


        #Registrador 1
        self.__reg1_11bits = numb & reg1_11bits_aux
        self.__reg1_11bits = self.__reg1_11bits >> 11


        #Registrador 2
        self.__reg2_11bits = numb & reg2_11bits_aux

        #print(bin(self.__opcode_4bits), bin(self.__verificador_2bits), bin(self.__tamanho_4bits),
        #      bin(self.__reg1_11bits), bin(self.__reg2_11bits))

