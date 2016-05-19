from doublex import *
from expects import *
from doublex_expects import *


class MemoryRepository:
    def __init__(self):
        self.values = {}

    def get(self, id):
        return self.values.get(id, 0)

    def set(self, id, value):
        self.values[id] = value


class Account:
    def __init__(self, id, repository):
        self.id = id
        self.repository = repository

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        value = self.repository.get(self.id)
        self.repository.set(self.id, value + amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        value = self.repository.get(self.id)
        if value - amount < 0:
            raise Exception("Not enough balance")
        self.repository.set(self.id, value - amount)

    @property
    def balance(self):
        return self.repository.get(self.id)




with description("Account"):
    with context('creates account'):
        with it("creates default account"):
            account = Account('an_id', MemoryRepository())
            expect(account.balance).to(equal(0))

    with context("deposit operation"):
        with before.each:
            self.account = Account('an_id', MemoryRepository())

        with it("can deposit"):
            self.account.deposit(5)
            self.account.deposit(2)

            expect(self.account.balance).to(equal(7))

        with it("cannot deposit negative amounts"):
            expect(lambda: self.account.deposit(-5)).to(raise_error(Exception))

        with it("cannot deposit 0 as amount"):
            expect(lambda: self.account.deposit(0)).to(raise_error(Exception))

    with context("withdrawal operations"):
        with before.each:
            repository = MemoryRepository()
            repository.set('an_id', 7)
            self.account = Account('an_id', repository)

        with it("can withdrawal if we have anough money"):
            self.account.withdraw(2)
            self.account.withdraw(1)
            expect(self.account.balance).to(equal(4))

        with it("cannot withdraw negative amounts"):
            expect(lambda: self.account.withdraw(-5)).to(raise_error(Exception))

        with it("cannot withdraw 0 as amount"):
            expect(lambda: self.account.withdraw(0)).to(raise_error(Exception))

        with it("cannot withdraw if doesn't have enough money"):
            expect(lambda: self.account.withdraw(10)).to(raise_error(Exception))


with description("Bank"):
    with context("Transfer"):
        with _it("transfer 100 from one account to another"):
            bank = Bank()
            bank.transfer('id_account1', 'id_account2', 100)
