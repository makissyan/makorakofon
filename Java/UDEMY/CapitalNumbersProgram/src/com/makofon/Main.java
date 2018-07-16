package com.makofon;



public class Main {

    public static boolean isPrimeNumber(int numberToCheck){
        int deviders = 0;

        for (int i = numberToCheck; i > 0; i--) {
            if (numberToCheck % i == 0)
                deviders++;
        }

        if (deviders < 3)
            return true;

        return false;
    }

    public static void printPrimeNumbers (int quantity){

        int counter = 0;
        for (int i = 2; counter < quantity; i++){

            if (isPrimeNumber(i)) {
                counter++;
                System.out.print("Number " + counter + " - " + i + "\n");
            }
        }
    }


    public static void main(String[] args) {

        printPrimeNumbers(8);

    }
}
