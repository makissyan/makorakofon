package com.makofon;

public class Car extends Vehicle {

    private char transmissionType;

    public Car(int wheels, int doors, int engine, int speed, char transmissionType) {
        super(wheels, doors, engine, speed);
        this.transmissionType = transmissionType;
    }

    public char getTransmissionType() {
        return transmissionType;
    }

    public void setTransmissionType(char transmissionType) {
        this.transmissionType = transmissionType;
    }

    public void changeTransmission(){

    switch (getTransmissionType()) {
        case 'A': System.out.print("You are automatic!\n");break;
        case 'M': System.out.print("You are manual!\n");break;
        default: System.out.print("Unknown transmission\n");break;

    }
        super.toGo(120);

    }

}
