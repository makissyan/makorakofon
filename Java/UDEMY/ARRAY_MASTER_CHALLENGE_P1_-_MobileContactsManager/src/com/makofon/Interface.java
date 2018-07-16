package com.makofon;

import java.util.Scanner;

public class Interface {

    Scanner input = new Scanner(System.in);

    MobileContactsManager ContactsList = new MobileContactsManager();

    public void printContactsList(){
        if (ContactsList.getSize() < 1)
            System.out.println("\nContacts list is empty");
        else {
            for (int i = 0; i < ContactsList.getSize(); i++) {
                System.out.println("\n\t" + (i+1) + " - " + ContactsList.getName(i) + " - " + ContactsList.getNumber(i));
                if (i + 1 == ContactsList.getSize())
                    System.out.println("\n");
                }
             }
    }

    public void addContact(){
        System.out.println("\nPlease enter phone number: \r");
        String number = input.next();
        System.out.println("\nPlease enter the name of contact: \r");
        String name = input.next();
        ContactEntry newContact = new ContactEntry(name, number);
        ContactsList.addToList(newContact);
    }

    public void removeContact(){
        System.out.println("\n Please enter NAME of contact which you'd like to delete: \r");
        String name = input.next();
        ContactsList.removeFromList(name);
    }

    public void editContact(){
        System.out.println("\nPlease enter ID of contact which you'd like to edit: \r");
        printContactsList();
        int index = input.nextInt()-1;
        if (index < ContactsList.getSize()) {
            System.out.println("\nPlease enter NEW NUMBER for contact " + (index+1) + "\r");
            String newPhone = input.next();
            System.out.println("\nPlease enter NEW NAME for contact " + (index+1) + "\r");
            String newName = input.next();
            ContactsList.editContact(index, newPhone, newName);
        }
        else
            System.out.println("\nIncorrect ID has been typed...");
    }
}
