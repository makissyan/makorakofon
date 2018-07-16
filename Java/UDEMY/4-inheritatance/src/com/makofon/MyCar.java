package com.makofon;

public class MyCar extends Car {

    private String model;

    public MyCar(int wheels, int doors, int engine, int speed, char transmissionType, String model) {
        super(wheels, doors, engine, speed, transmissionType);
        this.model = model;
    }

    public String getModel() {
        return model;
    }

    public void printModel() {
        System.out.print("Model: " + getModel() + "\n");
    }

}
