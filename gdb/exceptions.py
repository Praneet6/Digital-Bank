
class AccountException(Exception): pass
class InvalidAmountException(AccountException): pass
class InsufficientBalanceException(AccountException): pass
class MinimumBalanceViolationException(AccountException): pass
class InactiveAccountException(AccountException): pass
class InvalidPinException(AccountException): pass
