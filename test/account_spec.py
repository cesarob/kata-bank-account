from doublex import *
from expects import *
from doublex_expects import *


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

with description("Account"):
    with it("creates account"):
        account = Account()
        expect(account.balance).to(equal(0))

    with it("can deposit"):
        account = Account()
        amount = 5
        account.deposit(amount)
        expect(account.balance).to(equal(amount))

    with _it("can withdawl"):
        pass
