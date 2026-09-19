
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import AccountException

class FixedDepositAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, tenure_months, interest_rate):
        super().__init__(account_number, name, age, balance, "FIXEDDEPOSIT", status, pin)
        
    def process_debit(self, amount: float) -> None:
        raise AccountException("Premature withdrawals are not permitted on Fixed Deposit accounts")
