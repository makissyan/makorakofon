package com.makofon;

public class Main {

    public static void main(String[] args) {

        Hamburger hamburger = new Hamburger("Brown", "Beef");

        hamburger.addComponent("Lettuce", "Tomato", "Pickles");
        hamburger.addComponent("Mayo");
        hamburger.printBurger();

        Healthy_Burger healthyBurger = new Healthy_Burger();

        healthyBurger.addComponent("Onion", "Cheese", "Cheese", "Mayo", "Tomato", "Cucumber");
        healthyBurger.printBurger();
    }
}
