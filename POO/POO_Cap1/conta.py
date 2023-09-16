class Conta:

    def __init__(self,numero, titular,saldo,limite):
        print("Construindo Objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self,valor):
        print("Aqui alterar o limite")
        self.__limite = valor
    
    def extrato(self):
        print("Saldo R${}".format(self.__saldo))    
    
    def __saque_liberado(self,valor):
        return valor<=(self.__limite+self.__saldo)


    def sacar(self,valor):
        if(self.__saque_liberado(valor)):
            self.__saldo -= valor
            self.extrato()
        else:
            print("Conta com saldo insuficiente.")
    
    def depositar(self,valor):
        self.__saldo += valor
        self.extrato()
    
    def transferir(self,conta,valor):
        if(self.__saldo >= valor):
            self.sacar(valor)
            conta.depositar(valor)
            self.extrato()
        else:
            print("Saldo insuficiente para operação.")
    @staticmethod
    def codigo_banco():
        return "001"
    