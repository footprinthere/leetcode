from typing import Callable


class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance

    class OperationFailed(Exception): ...

    @staticmethod
    def _return_result(func: Callable[..., None]) -> Callable[..., bool]:
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Bank.OperationFailed:
                return False
            else:
                return True

        return wrapper

    @_return_result
    def transfer(self, account1: int, account2: int, money: int):
        self._validate_account(account1)
        self._validate_account(account2)
        self._check_balance(account1, money)

        self._incr_balance(account1, -1 * money)
        self._incr_balance(account2, money)

    @_return_result
    def deposit(self, account: int, money: int):
        self._validate_account(account)

        self._incr_balance(account, money)

    @_return_result
    def withdraw(self, account: int, money: int):
        self._validate_account(account)
        self._check_balance(account, money)

        self._incr_balance(account, -1 * money)

    def _validate_account(self, account: int):
        if not 1 <= account <= len(self.balance):
            raise Bank.OperationFailed

    def _check_balance(self, account: int, money: int):
        if self.balance[account - 1] < money:
            raise Bank.OperationFailed

    def _incr_balance(self, account: int, money: int):
        self.balance[account - 1] += money

    # FIXME: for test
    def run(self, op: str, args: list[int]) -> bool:
        print(f"{op} : {args}")
        if op == "withdraw":
            return self.withdraw(*args)
        elif op == "transfer":
            return self.transfer(*args)
        elif op == "deposit":
            return self.deposit(*args)


if __name__ == "__main__":
    ops = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    args = [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

    bank = Bank(args[0][0])
    results = [bank.run(op, a) for op, a in zip(ops[1:], args[1:])]

    print(results)
