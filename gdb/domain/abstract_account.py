
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
