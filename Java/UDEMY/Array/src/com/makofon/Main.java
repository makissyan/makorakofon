package com.makofon;

import java.util.Scanner;

public class Main {

    private static Scanner scanner = new Scanner(System.in);

    public static int[] createArray (int quantity) {
        int [] numbersArray = new int[quantity];
        System.out.print("Enter " + (quantity) + " elements: \r");
        for (int i=0; i<numbersArray.length; i++){
            numbersArray[i] = scanner.nextInt();
        }

        return numbersArray;

    }

    public static int[] sortArrByDesc (int[] arrayToSort){

        boolean flag = true;
        while (flag){
        flag = false;

        for(int i = 0; i<arrayToSort.length-1; i++){
            System.out.print("\n" + flag);
            int tmp = 0;
            int max = 0;
            if (arrayToSort[i] < arrayToSort[i+1]){
                    tmp = arrayToSort[i];
                    arrayToSort[i] = arrayToSort[i+1];
                    arrayToSort[i+1] = tmp;
                    flag = true;
            }
        }

        }
        return arrayToSort;
    }

    public static void printArray(int[] arrayToPrint) {
        for (int i=0; i<arrayToPrint.length; i++){
            System.out.print("\nElement " + i + " is: " + arrayToPrint[i]);
        }

    }

    public static void main(String[] args) {

        int[] sortedArr = sortArrByDesc(createArray(4));

        printArray(sortedArr);
    }
}
