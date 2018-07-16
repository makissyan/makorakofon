package com.company;

public class VipCustomer {

    private String name;
    private double creditLimit;
    private String emailAddress;

    VipCustomer () {
        this("John", 50, "inc@gni.to");
    }

    VipCustomer (String name, String emailAddress) {
        this(name, 100, emailAddress);
    }

    public void setCreditLimit(double creditLimit) {
        this.creditLimit = creditLimit;
    }

    VipCustomer (String name, double creditLimit, String emailAddress) {

        this.name = name;
        this.creditLimit = creditLimit;

        this.emailAddress = emailAddress;
    }

    public String getName() {
        return name;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public void showFullInfo() {
        System.out.print("\nNAME: " + this.getName());
        System.out.print("\nCREDIT LIMIT: " + this.getCreditLimit());
        System.out.print("\nE-MAIL: " + this.getEmailAddress());
    }
}
