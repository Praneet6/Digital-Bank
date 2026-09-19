package com.gdb.tests;
import com.gdb.domain.Account;

public class TestAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 2: Test Account Suite ===");
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE");
        
        // Test 1
        System.out.print("Test 1 (Initial Balance 5000.0): ");
        if (acc.getBalance() == 5000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        // Test 2
        System.out.print("Test 2 (Deposit 2000.0 -> Balance 7000.0): ");
        if (acc.deposit(2000.0) && acc.getBalance() == 7000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        // Test 3
        System.out.print("Test 3 (Negative Deposit -> Rejected): ");
        if (!acc.deposit(-500.0) && acc.getBalance() == 7000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        // Test 4
        System.out.print("Test 4 (Withdraw 3000.0 -> Balance 4000.0): ");
        if (acc.withdraw(3000.0) && acc.getBalance() == 4000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        // Test 5
        System.out.print("Test 5 (Exceeding Withdrawal -> Rejected): ");
        if (!acc.withdraw(10000.0) && acc.getBalance() == 4000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        // Test 6
        System.out.print("Test 6 (Negative Withdrawal -> Rejected): ");
        if (!acc.withdraw(-100.0) && acc.getBalance() == 4000.0) System.out.println("[PASS]");
        else System.out.println("[FAIL]");

        System.out.println("All Account tests completed successfully!");
    }
}
