from historic import Historic
from client import Client

class Account():
    
    def __init__(self, number, agency , client = Client, history = Historic):
        
        self.__number = number
        self.__agency = agency
        self.__client  = Client 
        self.__Historic= Historic

    @property
    def _balance(self):
        return self.__balance

    @_balance.setter
    def _balance(self, value):
        self.__balance = value

    @property
    def _number(self):
        return self.__number

    @_number.setter
    def _number(self, value):
        self.__number = value

    @property
    def _agency(self):
        return self.__agency

    @_agency.setter
    def _agency(self, value):
        self.__agency = value

    @property
    def _client(self):
        return self.__client

    @_client.setter
    def _client(self, value):
        self.__client = value

    @property
    def _Historic(self):
        return self.__Historic

    @_Historic.setter
    def _Historic(self, value):
        self.__Historic = value

        
    
   
    
    # def balance()->float:
    #     return 
        
    # def depositary(value = float)-> bool:
    #    return bool
   
    # def withdraw(valor = float)-> bool:
    #     return bool