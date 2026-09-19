import os

files = {
    "gdb/__init__.py": "",
    "gdb/domain/__init__.py": "",
    "gdb/tests/__init__.py": "",
    "gdb/exceptions.py": """
class AccountException(Exception): pass
class InvalidAmountException(AccountException): pass
class InsufficientBalanceException(AccountException): pass
class MinimumBalanceViolationException(AccountException): pass
class InactiveAccountException(AccountException): pass
class InvalidPinException(AccountException): pass
""",
    "gdb/domain/iaccount.py": """
from abc import ABC, abstractmethod

class IAccount(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> bool: pass
    
    @abstractmethod
    def withdraw(self, amount: float, entered_pin: str) -> None: pass
    
    @abstractmethod
    def get_balance(self) -> float: pass
    
    @abstractmethod
    def display_account_info(self) -> None: pass
    
    @abstractmethod
    def suspend(self) -> None: pass
    
    @abstractmethod
    def activate(self) -> None: pass
    
    @abstractmethod
    def close(self) -> None: pass
""",
    "gdb/domain/abstract_account.py": """
from abc import abstractmethod
from gdb.domain.iaccount import IAccount
from gdb.exceptions import *
from gdb.domain.account_rules_engine import AccountRulesEngine

class AbstractAccount(IAccount):
    def __init__(self, account_number, name, age, balance, account_type, status, pin):
        if age < 18: raise ValueError("Customer age must be at least 18.")
        if balance < 0: raise ValueError("Initial balance cannot be negative.")
        if not pin or len(pin) != 4 or not pin.isdigit(): raise ValueError("PIN must be exactly 4 digits.")
        
        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = status
        self.pin = pin
        self.rules_engine = AccountRulesEngine()

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def validate_pin(self, input_pin: str) -> bool:
        return self.pin == input_pin

    def withdraw(self, amount: float, entered_pin: str) -> None:
        if not self.validate_pin(entered_pin):
            raise InvalidPinException("Invalid PIN entered")
        if self.status != "ACTIVE":
            raise InactiveAccountException("Account is not active")
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive")
        
        self.rules_engine.validate_withdrawal(self, amount)
        self.process_debit(amount)

    @abstractmethod
    def process_debit(self, amount: float) -> None:
        pass

    def get_balance(self) -> float:
        return self.balance
        
    def display_account_info(self) -> None:
        pass
        
    def suspend(self) -> None: self.status = "SUSPENDED"
    def activate(self) -> None: self.status = "ACTIVE"
    def close(self) -> None: self.status = "CLOSED"
""",
    "gdb/domain/savings_account.py": """
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import MinimumBalanceViolationException

class SavingsAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, min_balance, interest_rate):
        super().__init__(account_number, name, age, balance, "SAVINGS", status, pin)
    
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
""",
    "gdb/domain/current_account.py": """
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import InsufficientBalanceException

class CurrentAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, overdraft_limit):
        super().__init__(account_number, name, age, balance, "CURRENT", status, pin)
        
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
""",
    "gdb/domain/fixed_deposit_account.py": """
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import AccountException

class FixedDepositAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, tenure_months, interest_rate):
        super().__init__(account_number, name, age, balance, "FIXEDDEPOSIT", status, pin)
        
    def process_debit(self, amount: float) -> None:
        raise AccountException("Premature withdrawals are not permitted on Fixed Deposit accounts")
""",
    "gdb/domain/salary_account.py": """
from gdb.domain.abstract_account import AbstractAccount
from gdb.exceptions import InsufficientBalanceException

class SalaryAccount(AbstractAccount):
    def __init__(self, account_number, name, age, balance, status, pin, employer_name):
        super().__init__(account_number, name, age, balance, "SALARY", status, pin)
        
    def process_debit(self, amount: float) -> None:
        self.balance -= amount
""",
    "gdb/domain/account_factory.py": """
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
""",
    "gdb/domain/account_rules_engine.py": """
import os

class AccountRulesEngine:
    def __init__(self):
        from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader
        self.loader = AccountRulesPropertiesLoader()
        self.rules = self.loader.load_all_rules()

    def get_minimum_balance(self, account_type: str) -> float:
        if account_type in self.rules and 'minBalance' in self.rules[account_type]:
            return float(self.rules[account_type]['minBalance'])
        # Fallback to defaults
        if account_type == "SAVINGS": return 1000.0
        return 0.0

    def get_interest_rate(self, account_type: str) -> float:
        if account_type in self.rules and 'interestRate' in self.rules[account_type]:
            return float(self.rules[account_type]['interestRate'])
        if account_type == "SAVINGS": return 4.0
        elif account_type == "FIXEDDEPOSIT": return 6.5
        return 0.0

    def get_overdraft_limit(self, account_type: str) -> float:
        if account_type in self.rules and 'overdraftLimit' in self.rules[account_type]:
            return float(self.rules[account_type]['overdraftLimit'])
        if account_type == "CURRENT": return 10000.0
        return 0.0

    def validate_withdrawal(self, account, amount: float) -> None:
        from gdb.exceptions import MinimumBalanceViolationException, InsufficientBalanceException
        min_balance = self.get_minimum_balance(account.account_type)
        overdraft_limit = self.get_overdraft_limit(account.account_type)

        if account.balance - amount < min_balance and min_balance > 0:
            raise MinimumBalanceViolationException("Breaches minimum balance")
        if account.balance - amount < -overdraft_limit:
            raise InsufficientBalanceException("Exceeds overdraft limit")
""",
    "gdb/domain/account_rules_properties_loader.py": """
import os

class AccountRulesPropertiesLoader:
    def __init__(self, config_dir="gdb/resources/config/rules"):
        self.config_dir = config_dir

    def load_properties(self, filepath):
        props = {}
        if not os.path.exists(filepath):
            return props
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    props[key.strip()] = val.strip()
        return props

    def load_all_rules(self):
        rules = {}
        if not os.path.exists(self.config_dir):
            return rules
            
        for filename in os.listdir(self.config_dir):
            if filename.endswith(".properties"):
                account_type = filename.split('.')[0].upper()
                rules[account_type] = self.load_properties(os.path.join(self.config_dir, filename))
        return rules
""",
    "gdb/tests/test_abstract_account.py": """
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import *

print("=== Activity 10: Abstract Account Test ===")
sa = SavingsAccount("SA1", "A", 20, 5000.0, "ACTIVE", "1234", 1000.0, 4.0)
ca = CurrentAccount("CA1", "B", 30, 5000.0, "ACTIVE", "1234", 10000.0)
fda = FixedDepositAccount("FD1", "C", 40, 50000.0, "ACTIVE", "1234", 12, 6.5)

try:
    sa.withdraw(4500.0, "1234")
    print("FAILED")
except MinimumBalanceViolationException:
    print("Caught MinimumBalanceViolationException [PASS]")
except Exception as e:
    print(f"FAILED {e}")

print("Test complete!")
""",
    "gdb/tests/test_interface_factory.py": """
from gdb.domain.account_factory import AccountFactory

print("=== Activity 12: Interface & Factory Test ===")
sa = AccountFactory.create_account("SAVINGS", "SA1", "A", 20, 5000.0, "ACTIVE", "1234", 1000.0, 4.0)
ca = AccountFactory.create_account("CURRENT", "CA1", "B", 30, 5000.0, "ACTIVE", "1234", 10000.0)
fda = AccountFactory.create_account("FIXEDDEPOSIT", "FD1", "C", 40, 5000.0, "ACTIVE", "1234", 12, 6.5)
salary = AccountFactory.create_account("SALARY", "SAL1", "D", 25, 5000.0, "ACTIVE", "1234", "Emp")

print("Created interfaces via Factory successfully!")
""",
    "gdb/tests/test_account_rules_engine.py": """
from gdb.domain.account_rules_engine import AccountRulesEngine

print("=== Activity 13: Rules Engine Test ===")
engine = AccountRulesEngine()
print(f"Savings Min Balance: {engine.get_minimum_balance('SAVINGS')}")
print(f"Savings Interest: {engine.get_interest_rate('SAVINGS')}")
print(f"Current Overdraft: {engine.get_overdraft_limit('CURRENT')}")
""",
    "gdb/tests/test_account_rules_engine_properties.py": """
from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

print("=== Activity 14: Rules Engine Properties Test ===")
engine = AccountRulesEngine()
print(f"Loaded config rules:")
print(f"Savings Min Balance: {engine.get_minimum_balance('SAVINGS')}")
""",
    "gdb/resources/config/rules/savings.properties": """minBalance=1000.0
interestRate=4.0
""",
    "gdb/resources/config/rules/current.properties": """overdraftLimit=10000.0
""",
    "gdb/resources/config/rules/fixeddeposit.properties": """interestRate=6.5
""",
    "gdb/resources/config/rules/salary.properties": """
"""
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("Files generated.")
