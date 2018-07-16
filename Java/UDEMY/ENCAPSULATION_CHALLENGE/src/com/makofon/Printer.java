package com.makofon;

public class Printer {

    private double tonerLevel = 60;
    private int pagesPrinted = 100;
    private boolean isDuplex = false;

    public Printer (int tonerLevel, int pagesPrinted, boolean isDuplex) {

        if ((tonerLevel > 0) && (tonerLevel <= 100)) {
            this.tonerLevel = tonerLevel;
        }
        if (pagesPrinted >= 0) {
            this.pagesPrinted = pagesPrinted;
        }
        this.isDuplex = isDuplex;
    }

    public Printer (int tonerLevel, int pagesPrinted) {

        if ((tonerLevel > 0) && (tonerLevel <= 100)) {
            this.tonerLevel = tonerLevel;
        }
        if (pagesPrinted >= 0) {
            this.pagesPrinted = pagesPrinted;
        }
    }

    public void fillToner (int addTonerValue) {

        if ((this.tonerLevel + addTonerValue) > 100) {
            System.out.print("\nToo much of new toner...\n" +
                    (100 - tonerLevel) + " was enough\n");
            this.tonerLevel = 100;
        }

        else {
            if (tonerLevel > 0) {
                this.tonerLevel += addTonerValue;
            }

            else {
                System.out.print("UNKNOWN VALUE");
            }
        }
    }

    public int printPage(){
        if (this.tonerLevel > 1) {
            System.out.print("\nPage has been successfully printed");
            this.pagesPrinted ++;
            this.tonerLevel -= 0.5;

            if (this.isDuplex == true) {
                this.pagesPrinted ++;
                this.tonerLevel -= 0.5;
            }
            return 1;
        }

        else
            return 2;
    }

    public void printTonerLevel () {
        System.out.print("\n**********\n" + this.tonerLevel + "\n*****\n");
    }

    public void printQuantity () {
        System.out.print("\n**********\n" + this.pagesPrinted + "\n*****\n");
    }

}
