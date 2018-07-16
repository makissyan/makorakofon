package com.makofon;

public class Main {

    public static void main(String[] args) {

        Printer myPrinter = new Printer(40,0);

        myPrinter.printTonerLevel();
        myPrinter.fillToner(100);
        myPrinter.printTonerLevel();

        for (int i = 105; i > 0; i-- ) {
            if (myPrinter.printPage() == 1)
                continue;
            else {
                System.out.print("\nOops... out of toner..." +
                        "\n REFILL ME ! ! !");
                myPrinter.fillToner(50);
            }
        }

        myPrinter.printTonerLevel();
        myPrinter.printQuantity();


    }
}
