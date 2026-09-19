
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
