#protected, private, public
class Bank:
    def __init__(self,name,balance,passport) -> None:
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #       print(self._name, self._balance, self._passport)
    
    def __print_privat_data(self):
          print(self.__name, self.__balance, self.__passport)
    def print(self):
        self.__print_privat_data()

account1 = Bank('Petr', 3877737, 6366333322)
account1.print()
print(dir(account1))
account1._Bank__print_privat_data()
