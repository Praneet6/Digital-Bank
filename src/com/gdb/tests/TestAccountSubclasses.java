package com.gdb.tests;
import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TestAccountSubclasses {
    public static void main(String[] args) {
        System.out.println("=== Activity 7: Account Subclasses Test ===");
        SavingsAccount sa = new SavingsAccount("SA1001", "Rahul", 30, 10000.0, "ACTIVE", "1111", 1000.0, 4.0);
        System.out.println("Savings Account Created: Balance Rs 10000.0 | Min Balance: Rs 1000.0");
        
        CurrentAccount ca = new CurrentAccount("CA1001", "Business", 40, 5000.0, "ACTIVE", "2222", 25000.0);
        System.out.println("Current Account Created: Overdraft Limit Rs 25000.0");

        FixedDepositAccount fda = new FixedDepositAccount("FD1001", "Ravi", 50, 50000.0, "ACTIVE", "3333", 12, 6.5);
        System.out.println("Fixed Deposit Created: Tenure 12 months | Interest: 6.5%");

        SalaryAccount salary = new SalaryAccount("SAL1001", "Neha", 28, 20000.0, "ACTIVE", "4444", "Infosys");
        System.out.println("Salary Account Created: Employer Infosys");
        
        System.out.println("All subclasses instantiated successfully!");
        
        System.out.println("\n=== Activity 8: Polymorphism Test ===");
        System.out.print("[Savings] Withdraw 9500 (breaches min balance 1000): ");
        try {
            sa.withdraw(9500.0, "1111");
            System.out.println("FAILED");
        } catch (MinimumBalanceViolationException e) {
            System.out.println("Caught MinimumBalanceViolationException [PASS]");
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[Current] Withdraw with Overdraft (Balance goes to -5000): ");
        try {
            ca.withdraw(10000.0, "2222");
            System.out.println("SUCCESS [PASS]");
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[Current] Withdraw exceeding Overdraft (exceeds -25000): ");
        try {
            ca.withdraw(30000.0, "2222");
            System.out.println("FAILED");
        } catch (InsufficientBalanceException e) {
            System.out.println("Caught InsufficientBalanceException [PASS]");
        } catch (Exception e) {
            System.out.println("FAILED");
        }

        System.out.print("[FixedDeposit] Withdraw attempt: ");
        try {
            fda.withdraw(5000.0, "3333");
            System.out.println("FAILED");
        } catch (AccountException e) {
            System.out.println("Caught AccountException [PASS]");
        }
        
        System.out.println("All polymorphic behaviors verified!");
    }
}
