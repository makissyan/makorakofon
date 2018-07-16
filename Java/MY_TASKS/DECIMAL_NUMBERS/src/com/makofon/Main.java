package com.makofon;

import java.util.ArrayList;
import java.util.List;

public class Main {

    //function to divide input integer per digits
    public static List<Integer> divideNumber(int inputNumber) {
        List<Integer> numberByDigits = new ArrayList<Integer> ();

        while (inputNumber > 0) {

            numberByDigits.add(0, inputNumber%10);
            inputNumber = inputNumber / 10;
        }

        return numberByDigits;
    }
    //function to compose decimal number from two List<Integer> objects
    public static List<Integer> decimalNumber(List<Integer> firstNumbersList, List<Integer> secondNumbersList) {
        List<Integer> decimalNumber = new ArrayList<Integer>();
        int decimalNumberSize = firstNumbersList.size() + secondNumbersList.size();

        for (int positionToInsert = 0; positionToInsert <= decimalNumberSize; positionToInsert++){

            if(positionToInsert < firstNumbersList.size()) {
                decimalNumber.add(firstNumbersList.get(positionToInsert));
            }

            if(positionToInsert < secondNumbersList.size()) {
                decimalNumber.add(secondNumbersList.get(positionToInsert));
            }
        }

        return decimalNumber;
   }

    public static void main(String[] args) {
        System.out.print("\n"+decimalNumber(divideNumber(111357910), divideNumber(22468)));
    }
}
