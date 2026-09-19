
from gdb.domain.account_rules_engine import AccountRulesEngine

print("=== Activity 13: Rules Engine Test ===")
engine = AccountRulesEngine()
print(f"Savings Min Balance: {engine.get_minimum_balance('SAVINGS')}")
print(f"Savings Interest: {engine.get_interest_rate('SAVINGS')}")
print(f"Current Overdraft: {engine.get_overdraft_limit('CURRENT')}")
