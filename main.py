class Account():

    def __init__(self, id, balance = 0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money >0:
            self.balance += money
            print(f"You add money. Sum on id: {self.balance}")

    def withdraw(self, money):
        if self.balance < money:
            print('не хватает денег')
        elif self.balance > money:
            self.balance -= money
            print(f'вы успешно сняли {money}. Остаток: {self.balance}')

man = Account(111, 600)
print(man.balance)
man.withdraw(200)
print(man.balance)
man.withdraw(1000)
print(man.balance)
man.deposit(2300)
print(man.balance)


