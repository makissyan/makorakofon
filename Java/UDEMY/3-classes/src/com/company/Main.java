package com.company;

public class Main {

    public static void printDevider() {
        System.out.println("\n************************************");
    }

    public static void main(String[] args) {
        Car porsche = new Car();
        porsche.setModel("Cayenne");

        System.out.println("Model is " + porsche.getModel());
        printDevider();

        BankAccount account = new BankAccount();

        account.printBalance();
        account.makeDeposit(100);
        account.printBalance();
        account.withdraw(1000);
        account.withdraw(95.72);
        account.withdraw(30);

        printDevider();

        VipCustomer Max = new VipCustomer("Maksym Melanchenko", 5000,
                "makofon@program.mer");
        VipCustomer Ola = new VipCustomer("Olga Pereguda", "p@regu.don");
        VipCustomer Unknown = new VipCustomer();
        Max.showFullInfo();
        printDevider();
        Ola.showFullInfo();
        printDevider();
        Unknown.showFullInfo();

        printDevider();

        Max.setCreditLimit(account.getCustomerBalance() + 10000);
        Max.showFullInfo();
        System.out.print("\n" + Max);
    }
}
