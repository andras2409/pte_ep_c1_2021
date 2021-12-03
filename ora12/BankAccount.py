class BankAccount:
    def __init__(self, name: str, account_number: int, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyelneg_kiiratas(self):
        print(self.balance)

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawal(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print("Sikeres pénzfelvétel!")
        else:
            print("Sikertelen pénzfelvétel!")

account1 = BankAccount("Béla", "0000000000", 100000)
account2 = BankAccount("Béla", "1111111111")
account1.egyelneg_kiiratas()
account2.egyelneg_kiiratas()
account1.withdrawal(50000)
account2.withdrawal(50000)
account1.egyelneg_kiiratas()
account2.egyelneg_kiiratas()
account1.deposit(20000)
account2.deposit(20000)
account1.egyelneg_kiiratas()
account2.egyelneg_kiiratas()