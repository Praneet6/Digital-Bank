
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import InsufficientBalanceException

class CurrentAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, overdraft_limit):
        super().__init__(account_number, name, age, balance, "CURRENT", status, pin)
        
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
