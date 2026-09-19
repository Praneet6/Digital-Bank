
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
