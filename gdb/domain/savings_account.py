
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import MinimumBalanceViolationException

class SavingsAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, min_balance, interest_rate):
        super().__init__(account_number, name, age, balance, "SAVINGS", status, pin)
    
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
