package com.makofon;

public class Healthy_Burger extends Hamburger {

    private int components = 6;
    private String[] additionalComponents = new String [components];

    public Healthy_Burger(){
        super("Brown Rye", "Soy");
        super.setName("Healthy burger");
        super.setSauceType("Sour cream");
        super.setComponents(this.components);
    }

}
