
from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

print("=== Activity 14: Rules Engine Properties Test ===")
engine = AccountRulesEngine()
print(f"Loaded config rules:")
print(f"Savings Min Balance: {engine.get_minimum_balance('SAVINGS')}")
