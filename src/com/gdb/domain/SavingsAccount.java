package com.gdb.domain;
import com.gdb.exceptions.*;

public class SavingsAccount extends AbstractAccount {
    private double minBalance;
    private double interestRate;

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, double minBalance, double interestRate) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
        this.minBalance = minBalance;
        this.interestRate = interestRate;
    }

    public void applyInterest() {
        this.balance += this.balance * (interestRate / 100.0);
    }

    @Override
    protected void processDebit(double amount) throws AccountException {
        if (this.balance - amount < minBalance) {
            throw new MinimumBalanceViolationException("Breaches minimum balance");
        }
        this.balance -= amount;
    }
}
