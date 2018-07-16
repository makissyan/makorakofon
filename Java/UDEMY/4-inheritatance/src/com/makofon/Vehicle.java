package com.makofon;

public class Vehicle {

    private int wheels;
    private int doors;
    private int engine;
    private int speed;

    public Vehicle(int wheels, int doors, int engine, int speed) {
        this.wheels = wheels;
        this.doors = doors;
        this.engine = engine;
        this.speed = speed;
    }

    public int getWheels() {
        return wheels;
    }

    public void setWheels(int wheels) {
        this.wheels = wheels;
    }

    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    public int getEngine() {
        return engine;
    }

    public void setEngine(int engine) {
        this.engine = engine;
    }

    public int getSpeed() {
        return speed;
    }

    public void toGo (int speed) {
        this.speed = speed;
        System.out.print("Speed: " + this.getSpeed() + "\n");

    }

    public void steering() {
        System.out.print("It's controllable...\n");
    }
}
