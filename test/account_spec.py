from doublex import *
from expects import *
from doublex_expects import *

class MemoryRepository:
    def __init__(self):
        self.value = 0

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

class Account:
    def __init__(self, repository):
        self.repository = repository

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        value = self.repository.get()
        self.repository.set(value + amount)

    @property
    def balance(self):
        return self.repository.get()


with description("Account"):
    with context('creates account'):
        with it("creates default account"):
            account = Account(MemoryRepository())
            expect(account.balance).to(equal(0))

    with context("deposit operation"):
        with before.each:
            self.account = Account(MemoryRepository())

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
            self.account = Account(MemoryRepository())
