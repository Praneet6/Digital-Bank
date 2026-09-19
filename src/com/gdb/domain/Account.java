package com.gdb.domain;
import com.gdb.exceptions.*;

public class Account {
    private String accountNumber;
    private String name;
    private int age;
    private double balance;
    private String accountType;
    private String status;
    private String pin;

    public Account(String accountNumber, String name, int age, double balance, String accountType, String status) {
        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = balance;
        this.accountType = accountType;
        this.status = status;
    }

    public Account(String accountNumber, String name, int age, double balance, String accountType, String status, String pin) {
        if (age < 18) throw new IllegalArgumentException("Age must be at least 18");
        if (balance < 0) throw new IllegalArgumentException("Balance cannot be negative");
        if (pin == null || pin.length() != 4 || !pin.matches("\\d{4}")) throw new IllegalArgumentException("PIN must be 4 digits");
        
        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = balance;
        this.accountType = accountType;
        this.status = status;
        this.pin = pin;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
            return true;
        }
        return false;
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            this.balance -= amount;
            return true;
        }
        return false;
    }

    public boolean withdraw(double amount, String enteredPin) throws AccountException {
        if (!validatePin(enteredPin)) throw new InvalidPinException("Invalid PIN entered");
        if (!"ACTIVE".equals(status)) throw new InactiveAccountException("Account is not active");
        if (amount <= 0) throw new InvalidAmountException("Withdrawal amount must be positive");
        if (amount > balance) throw new InsufficientBalanceException("Insufficient funds in account");
        
        this.balance -= amount;
        return true;
    }

    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Balance: Rs " + balance);
        System.out.println("Account Type: " + accountType);
        System.out.println("Status: " + status);
    }

    public boolean validatePin(String inputPin) {
        return this.pin != null && this.pin.equals(inputPin);
    }

    public boolean changePin(String oldPin, String newPin) {
        if (validatePin(oldPin)) {
            if (newPin != null && newPin.length() == 4 && newPin.matches("\\d{4}")) {
                this.pin = newPin;
                return true;
            }
        }
        return false;
    }

    public void suspend() { this.status = "SUSPENDED"; }
    public void activate() { this.status = "ACTIVE"; }
    public void close() { this.status = "CLOSED"; }

    public double getBalance() { return balance; }
}
