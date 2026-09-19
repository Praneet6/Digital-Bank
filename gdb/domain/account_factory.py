
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.domain.salary_account import SalaryAccount

class AccountFactory:
    @staticmethod
    def create_account(account_type, *args):
        if account_type == "SAVINGS":
            return SavingsAccount(*args)
        elif account_type == "CURRENT":
            return CurrentAccount(*args)
        elif account_type == "FIXEDDEPOSIT":
            return FixedDepositAccount(*args)
        elif account_type == "SALARY":
            return SalaryAccount(*args)
        else:
            raise ValueError(f"Unknown account type {account_type}")
