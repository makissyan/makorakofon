package com.makofon;

public class Window {
    private int quantity;
    private char category;

    public Window(int quantity, char category){
        this.quantity = quantity;
        this.category = category;
    }

    private char getCategory(){
        return this.category;
    }
}
