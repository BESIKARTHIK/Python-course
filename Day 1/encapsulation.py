class Bank:

    def __init__(self):
        self.balance = 10000

    def show_balance(self):
        print(self.balance)

account = Bank()

account.show_balance()

class Bank:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print(self.__balance)

account = Bank()

account.show_balance()