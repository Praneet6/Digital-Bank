package com.gdb.tests;
import com.gdb.domain.Account;
import com.gdb.exceptions.*;

public class TestAccountExceptions {
    public static void main(String[] args) {
        System.out.println("=== Activity 6: Exception Handling Suite ===");
        
        Account acc1 = new Account("ACC1002", "Amit", 25, 5000.0, "SAVINGS", "ACTIVE", "1234");
        
        System.out.print("[Test 1] ");
        try {
            acc1.withdraw(1000.0, "9999");
            System.out.println("Failed: Exception not thrown");
        } catch (InvalidPinException e) {
            System.out.println("Caught Invalid PIN: " + e.getMessage() + " [PASS]");
        } catch (Exception e) {
            System.out.println("Caught unexpected exception [FAIL]");
        }

        System.out.print("[Test 2] ");
        acc1.suspend();
        try {
            acc1.withdraw(1000.0, "1234");
            System.out.println("Failed: Exception not thrown");
        } catch (InactiveAccountException e) {
            System.out.println("Caught Inactive Account: " + e.getMessage() + " [PASS]");
        } catch (Exception e) {
            System.out.println("Caught unexpected exception [FAIL]");
        }

        System.out.print("[Test 3] ");
        acc1.activate();
        try {
            acc1.withdraw(-500.0, "1234");
            System.out.println("Failed: Exception not thrown");
        } catch (InvalidAmountException e) {
            System.out.println("Caught Invalid Amount: " + e.getMessage() + " [PASS]");
        } catch (Exception e) {
            System.out.println("Caught unexpected exception [FAIL]");
        }

        System.out.print("[Test 4] ");
        try {
            acc1.withdraw(10000.0, "1234");
            System.out.println("Failed: Exception not thrown");
        } catch (InsufficientBalanceException e) {
            System.out.println("Caught Insufficient Funds: " + e.getMessage() + " [PASS]");
        } catch (Exception e) {
            System.out.println("Caught unexpected exception [FAIL]");
        }

        System.out.print("[Test 5] ");
        acc1.close();
        try {
            acc1.withdraw(1000.0, "1234");
            System.out.println("Failed: Exception not thrown");
        } catch (AccountException e) {
            System.out.println("Polymorphic Handler caught: " + e.getMessage() + " [PASS]");
        } catch (Exception e) {
            System.out.println("Caught unexpected exception [FAIL]");
        }
        
        System.out.println("All exception handling tests completed successfully!");
    }
}
