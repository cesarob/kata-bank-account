from doublex import *
from expects import *
from doublex_expects import *


class MemoryRepository:
    def __init__(self):
        self.values = {}

    def get(self, id):
        return self.values.get[od]

    def set(self, id, value):
        self.values[id] = value


class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        if self.balance - amount < 0:
            raise Exception("Not enough balance")
        self.balance -= amount


class Bank:
    def __init__(self, repository):
        pass


with description("Account"):
    with context('creates account'):
        with it("creates default account"):
            account = Account('an_id')
            expect(account.balance).to(equal(0))

    with context("deposit operation"):
        with before.each:
            self.account = Account('an_id')

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
            self.account = Account('an_id')
            self.account.balance = 7

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
            pass
            # repository = MemoryRepository()
            # account1 = given_an_account('id_account1', repository, 100)
            # account2 = given_an_account('id_account2', repository, 0)
            #
            # bank = Bank()
            # bank.transfer('id_account1', 'id_account2', 100)
            # expect(account1.balance).to(equal(0))
            # expect(account1.balance).to(equal(100))


def given_an_account(id_account, repository, amount):
    account = Account(id_account, repository)
    if amount > 0:
        account.deposit(amount)
    return account
