class BankAccount:
    def __init__(self) -> None:
        self.balance = 0
        # self.is_money_valid = lambda money: False if money < 0 else True

    def deposit(self, money):
        if self.is_money_valid(money):
            self.balance += money

    def is_money_valid(self, money):
        if money < 0:
            print("Invalid operation")
            return False
        return True

    def withdraw(self, money):
        if self.is_money_valid(money):
            if self.balance - money < 0:
                print("Money withdrawn exceeds balance")
                return
            self.balance -= money

    def show_balance(self):
        print(self.balance)


b_account1 = BankAccount()
b_account1.show_balance()
b_account1.deposit(4000)
b_account1.withdraw(455)
b_account1.deposit(3000)
b_account1.withdraw(8000)
b_account1.show_balance()
# b_account2 = BankAccount()
# b_account2.show_balance()
# b_account2.deposit(100)
# b_account2.show_balance()
# b_account2.withdraw(90)
# b_account2.show_balance()
