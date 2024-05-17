from account import Account
from transaction import Transaction



class Client(Account,Transaction):
    def __init__(self,address,accounts):
        self.__address = address
        self.__accounts = accounts

    @property
    def _accounts(self):
        return self.__accounts

    @_accounts.setter
    def _accounts(self, value):
        self.__accounts = []
 

    @property
    def _address(self):
        return self.__address

    @_address.setter
    def _address(self, value):
        self.__address = value

    def get_accounts(self):
        return self.accounts

    def set_accounts(self, value):
        self.accounts = value

    
    # def add_account(account = Account):
    #     pass
    
    # def carry_out_transaction(account = Account, transaction=Transaction)-> None:
    #     pass