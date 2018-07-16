package com.makofon;

import java.util.ArrayList;

public class GroceryList {

    private ArrayList<String> groceryList = new ArrayList<String>();

    public void addGroceryItem(String item) {
            groceryList.add(item);
    }

    public void printGroceryList() {
        System.out.println("You have " + groceryList.size() + " items in your grocery list:");
        for (int i = 0; i<groceryList.size(); i++){
            System.out.println("\n - "+ groceryList.get(i));
        }
    }
}
