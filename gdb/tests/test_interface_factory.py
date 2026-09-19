
from gdb.domain.account_factory import AccountFactory

print("=== Activity 12: Interface & Factory Test ===")
sa = AccountFactory.create_account("SAVINGS", "SA1", "A", 20, 5000.0, "ACTIVE", "1234", 1000.0, 4.0)
ca = AccountFactory.create_account("CURRENT", "CA1", "B", 30, 5000.0, "ACTIVE", "1234", 10000.0)
fda = AccountFactory.create_account("FIXEDDEPOSIT", "FD1", "C", 40, 5000.0, "ACTIVE", "1234", 12, 6.5)
salary = AccountFactory.create_account("SALARY", "SAL1", "D", 25, 5000.0, "ACTIVE", "1234", "Emp")

print("Created interfaces via Factory successfully!")
