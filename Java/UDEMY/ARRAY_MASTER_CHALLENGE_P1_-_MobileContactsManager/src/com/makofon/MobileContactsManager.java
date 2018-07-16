package com.makofon;

import java.util.ArrayList;


public class MobileContactsManager {
    private ArrayList<ContactEntry> contactsList = new ArrayList<ContactEntry>();

    public int getSize(){
        return this.contactsList.size();
    }

    public String getName(int index){
        return this.contactsList.get(index).getName();
    }

    public String getNumber(int index){
        return this.contactsList.get(index).getNumber();
    }

    public void addToList(ContactEntry contact){
        this.contactsList.add(contact);
    }

    public void removeFromList(String name){
        name = name.toUpperCase();
        boolean isFound = false;

        for (int i = 0; i < contactsList.size(); i++){
            if (contactsList.get(i).getName().toUpperCase().equals(name)){
                isFound = true;
                this.contactsList.remove(i);
                System.out.println("\nContact " + name + " has been deleted");
                break;
            }
        }
        if (!isFound)
            System.out.println("Unable to find " + name);
    }

    public void editContact(int index, String number, String name){

        this.contactsList.get(index).editNumber(number);
        this.contactsList.get(index).editName(name);

    }
}
