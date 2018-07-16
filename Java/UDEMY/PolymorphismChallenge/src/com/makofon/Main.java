package com.makofon;

class Car {

    private boolean engine = true;
    private int cylinders;
    private int wheels = 4;
    private String name;

    public Car (int cylinders, String name) {
        this.cylinders = cylinders;
        this.name = name;
    }

    public void printName(){
        System.out.print("Name - " + this.name + "\n");
    }

    public void engineSound(){
        System.out.print("Soft sound\n");
    }
}


class Subaru extends Car {

    public Subaru(){
        super(4, "Subaru");
    }

    public void engineSound() {
        System.out.print("Agressive sound!\n");
    }
}

class FordMustang extends Car{

    public FordMustang(){
        super(6, "Ford Mustang");
    }

    @Override
    public void engineSound(){
        System.out.print("A really-really powerful sound!");
    }

}

class Chevrolet extends Car {

    public Chevrolet(){
        super(2, "Chevrolet Aveo");
    }

    public void engineSound(){
        System.out.print("Easy-peasy-softy sound");
    }
}



public class Main {

    public static void main(String[] args) {

        Car subaru = new Subaru();
        Car mustang = new FordMustang();
        Car chevrolet = new Chevrolet();

        subaru.printName();
        subaru.engineSound();

        System.out.print("\n\n");

        mustang.printName();
        mustang.engineSound();

        System.out.print("\n\n");

        chevrolet.printName();
        chevrolet.engineSound();

    }
}
