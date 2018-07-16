
package com.makofon;
public class Hamburger {

    private String name;
    private String breadType;
    private String meatType;
    private String sauceType;
    private int components;
    private String[] additionalComponents;
    private double price = 3.0;

    public Hamburger(String breadType, String meatType) {
        this.name = "Hamburger";
        this.breadType = breadType;
        this.meatType = meatType;
        this.sauceType = "Ketchup";
        this.components = 4;
    }


    public String getName() {
        return name;
    }

    public String getBreadType() {
        return breadType;
    }

    public String getMeatType() {
        return meatType;
    }

    public String getSauceType() {
        return sauceType;
    }

    public double getPrice() {
        return price;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setBreadType(String breadType) {
        this.breadType = breadType;
    }

    public void setMeatType(String meatType) {
        this.meatType = meatType;
    }

    public void setSauceType(String sauceType) {
        this.sauceType = sauceType;
    }

    public void setComponents(int components) {
        this.components = components;
    }

    public int addComponent(String... component){
        if (this.additionalComponents == null)
            this.additionalComponents = new String[components];

        if (component.length > this.additionalComponents.length){
            System.out.print("\nToo much additional components\n");
            return -1;
        }

        for (String tmpComponent : component){

            for (int i = 0; i < this.components; i++) {
                if (this.additionalComponents[i] == null) {
                    this.additionalComponents[i] = tmpComponent;
                    this.price += 0.5;
                    break;
                }

            }

        }

        return 0;

    }


    public String printPrice() {

        String formatedPrice = String.format("%.2f", price);
        System.out.print("\nPrice: " + formatedPrice + "\n\n");
        return formatedPrice;
    }

    public String printAdditionalComponents() {

        String additionalComponents = "";

        for (int i = 0; i < this.additionalComponents.length; i++) {

            if (this.additionalComponents[i] != null)
                additionalComponents += "\n\t - " + this.additionalComponents[i] + "; ";

            else
                break;
        }
        return additionalComponents;
    }

    public void printBurger(){
        System.out.print("\n---\nYour choice: " + getName());
        System.out.print("\n\tBread: " + getBreadType());
        System.out.print("\n\tMeat: " + getMeatType());
        System.out.print("\n\tSauce: " + getSauceType());
        if (!printAdditionalComponents().equals(""))
            System.out.print("\n\tAdditional components:" + printAdditionalComponents());
        System.out.print("\n----------");
        printPrice();
    }
}
