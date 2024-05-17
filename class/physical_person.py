from client import Client


class Physical_Person(Client):
    
    
    def __init__(self,cpf,nome,date_of_birth, address):
        super().__init__(address)
        self.__cpf = cpf
        self.__nome = nome
        self.__date_of_birth = date_of_birth

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _date_of_birth(self):
        return self.__date_of_birth

    @_date_of_birth.setter
    def _date_of_birth(self, value):
        self.__date_of_birth = value
