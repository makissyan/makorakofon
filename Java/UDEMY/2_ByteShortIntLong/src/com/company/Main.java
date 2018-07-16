package com.company;

public class Main {


    public static double calcFeetAndInchesToCentimeters(double startInches) {


        if (startInches > 0) {
            double a;
            a = startInches * 10;
            System.out.println("\n" + a);
            System.out.println("********************");
            return a;
        } else {
            return -1;
        }

    }

    public static double calculateInterest(double amount, double interestRate) {
        return (amount * (interestRate / 100));
    }

    public static int switcher(char switchChar){

        switch (switchChar) {

        case 'A':
            System.out.println("A");
            break;
        case 'B':
            System.out.println("B");
            break;
        case 'C':
        case 'D':
        case 'E':
            System.out.println("C, D, or E");
            break;
        default:
            System.out.println("Yo though");
            break;
        }
        System.out.println("********************");
        return 0;
    }

    public static boolean isPrimeNumber(int x) {

        int deviders = 0;
        for (int i = x; x>=1; x --) {

            if (i % x == 0) {
                deviders ++;

            }
        }
        if (deviders == 2) {
            return true;
        }
        else
            return false;
    }

    public static double generateFibonacci(int quanitity) {

        double fibon = 0;
        double prevNumber = 0;
        int counter = 0;
        for (double i = 0; counter<quanitity; i=fibon){
            if (i == 0) {
                i ++;
            }
            fibon = i+prevNumber;
            prevNumber = i;
            counter ++;
            System.out.println("Fibonacci " + counter + " - " + fibon);

        }
        System.out.println("********************");
        return 0;

    }

    public static double generatePrimeNumbers(int quantity) {
        int primeCounter = 0;

            for (int i = 1; primeCounter < quantity; i++) {
        if (isPrimeNumber(i)) {
            System.out.println("Prime number " + (primeCounter+1) + " - " + i);
            primeCounter++;
        }


    }
        System.out.println("********************");
        return 0;
    }

    public static boolean isEvenNumber (int number) {

        if (number % 2 == 0) {
            return true;
        }
        else
            return false;
    }

    public static int evenNumbers (int quantity, int startPoint) {

        System.out.println("********************");
        int counter = 1;

        while (counter <= quantity) {

            if (!isEvenNumber(startPoint)) {
                startPoint++;
                continue;
            }

            System.out.println("Even number" + counter + " - " + startPoint);
            startPoint++;
            counter++;
            }

        return 0;
        }


    public static void main(String[] args) {

        generateFibonacci(5);

    }
}