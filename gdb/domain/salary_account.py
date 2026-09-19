
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import InsufficientBalanceException

class SalaryAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, employer_name):
        super().__init__(account_number, name, age, balance, "SALARY", status, pin)
        
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
