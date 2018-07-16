package com.makofon;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Interface go = new Interface();

        int menu = 0;
        Scanner menuInput = new Scanner(System.in);
        boolean quit = false;

        while (!quit){

            System.out.println("\nPlease make your choice...\n");
            System.out.println("\n1 - Add contact");
            System.out.println("\n2 - Print contacts list");
            System.out.println("\n3 - Edit contact");
            System.out.println("\n4 - Remove contact");
            System.out.println("\n5 - Quit");
            menu = menuInput.nextInt();
            switch (menu) {
                case 1 : go.addContact(); break;
                case 2 : go.printContactsList(); break;
                case 3 : go.editContact(); break;
                case 4 : go.removeContact(); break;
                case 5 : quit = true; break;
                default : System.out.println("Incorrect choice...");
            }
            menu = 0;
        }
    }
}

