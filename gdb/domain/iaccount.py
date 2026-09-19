
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
