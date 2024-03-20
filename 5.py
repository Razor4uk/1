class Bankaccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        return f"Баланс на счете номер {self.account_number} владельца {self.owner} составляет {self.balance}"


account = Bankaccount("Олег Олегович", "9438762878", 2367)
print(account.show_balance())
