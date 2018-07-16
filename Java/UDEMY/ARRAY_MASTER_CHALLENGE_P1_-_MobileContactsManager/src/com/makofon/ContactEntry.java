package com.makofon;

public class ContactEntry {
    private String name;
    private String number;

    public ContactEntry (String name, String number) {
        this.name = name;
        this.number = number;
    }

    protected void editNumber (String number){
        this.number = number;
        }

    protected void editName(String name){
        this.name = name;
        }

    protected String getName() {
        return this.name;
    }

    protected String getNumber() {
        return this.number;
    }
}

