package com.gdb.tests;
import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TestAbstractAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 9: Abstract Account & Template Pattern ===");
        SavingsAccount sa = new SavingsAccount("SA1001", "Rahul", 30, 10000.0, "ACTIVE", "1111", 1000.0, 4.0);
        CurrentAccount ca = new CurrentAccount("CA1001", "Business", 40, 5000.0, "ACTIVE", "2222", 25000.0);
        FixedDepositAccount fda = new FixedDepositAccount("FD1001", "Ravi", 50, 50000.0, "ACTIVE", "3333", 12, 6.5);
        
        System.out.print("[Savings] Withdraw 2000: ");
        try {
            sa.withdraw(2000.0, "1111");
            System.out.println("SUCCESS | Balance: Rs " + sa.getBalance());
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[Savings] Withdraw below min balance: ");
        try {
            sa.withdraw(8000.0, "1111");
            System.out.println("FAILED");
        } catch (MinimumBalanceViolationException e) {
            System.out.println("Caught MinimumBalanceViolationException [PASS]");
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[Current] Overdraft debit: ");
        try {
            ca.withdraw(8000.0, "2222");
            System.out.println("SUCCESS | Balance: Rs " + ca.getBalance());
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[FixedDeposit] Premature debit: ");
        try {
            fda.withdraw(5000.0, "3333");
            System.out.println("FAILED");
        } catch (AccountException e) {
            System.out.println("Caught AccountException [PASS]");
        }

        System.out.println("Template method pattern executed successfully!");
    }
}
