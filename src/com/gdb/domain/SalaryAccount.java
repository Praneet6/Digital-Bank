package com.gdb.domain;
import com.gdb.exceptions.*;

public class SalaryAccount extends AbstractAccount {
    private String employerName;
    private int inactiveMonths;

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin, String employerName) {
        super(accountNumber, name, age, balance, "SALARY", status, pin);
        this.employerName = employerName;
        this.inactiveMonths = 0;
    }

    @Override
    protected void processDebit(double amount) throws AccountException {
        if (amount > this.balance) {
            throw new InsufficientBalanceException("Insufficient funds in account");
        }
        this.balance -= amount;
    }
}
