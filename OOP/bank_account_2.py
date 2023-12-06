class Bank_Account:
    def __init__(self, owner) -> None:
        self.balance = 0
        self.owner = owner

    def is_money_negative(self, money):
        if money < 0:
            print("Значение денег отрицательное")
            return True
        return False

    def deposit(self, money):
        if not self.is_money_negative(money):
            self.balance += money
            print(f"Счёт пополнен на ${money}")

    def withdraw(self, money):
        if not self.is_money_negative(money):
            if money > self.balance:
                print("Запрашиваемые деньги больше баланса")
                return
            self.balance -= money
            print(f"Со счета снято ${money}")

    def show_balance(self):
        print(self.balance)


class Owner:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"


owner_1 = Owner("Azamat", "Isakov")

account_1 = Bank_Account(owner_1)
account_1.deposit(3000)
account_1.show_balance()

print(account_1.owner.get_fullname())

account_1.withdraw(5000)
account_1.show_balance()
