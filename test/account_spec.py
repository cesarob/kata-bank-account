from doublex import *
from expects import *
from doublex_expects import *


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise Exception("Invalid amount")
        self.balance += amount


with description("Account"):
    with it("creates account"):
        account = Account()
        expect(account.balance).to(equal(0))

    with context("deposit operation"):
        with before.all:
            self.account = Account()

        with it("can deposit"):
            self.account.deposit(5)
            expect(self.account.balance).to(equal(5))

        with it("cannot deposit negative amounts"):
            expect(lambda: self.account.deposit(-5)).to(raise_error(Exception))
