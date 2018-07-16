package com.company;

public class BankAccount {

    private int customerAccountNumber;
    private double customerBalance;
    private String customerName;
    private String customerEmail;
    private String customerPhone;

    public int getCustomerAccountNumber() {
        return customerAccountNumber;
    }

    public double getCustomerBalance() {
        return customerBalance;
    }

    public String getCustomerName() {
        return customerName;
    }

    public String getCustomerEmail() {
        return customerEmail;
    }

    public String getCustomerPhone() {
        return customerPhone;
    }

    public void setCustomerAccountNumber(int customerAccountNumber) {
        this.customerAccountNumber = customerAccountNumber;
    }

    private void setCustomerBalance(double customerBalance) {
        this.customerBalance = customerBalance;
    }

    public void setCustomerEmail(String customerEmail) {
        this.customerEmail = customerEmail;
    }

    public void setCustomerPhone(String customerPhone) {
        this.customerPhone = customerPhone;
    }

    public float makeDeposit (float deposit) {

        this.setCustomerBalance(deposit);
        System.out.println("Balance has been updated with: " + deposit + " UAH");
        return 0;
    }

    public void withdraw (double amount) {
        if (amount > getCustomerBalance()) {
            System.out.println("Unable to withdraw " + amount + ".");
            this.printBalance();
        }

        else {
            double tmp = getCustomerBalance();
            System.out.println(amount + " has been withdrawed.");
            tmp -= amount;
            setCustomerBalance(tmp);
        }

    }

    public void printBalance () {
        System.out.println("Current balance: " + this.getCustomerBalance() + " UAH.");
    }

}

