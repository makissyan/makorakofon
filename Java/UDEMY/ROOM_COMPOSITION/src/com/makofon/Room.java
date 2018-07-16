package com.makofon;

public class Room {
    private double size;
    private char floorCode;
    private Furniture furniture;
    private Door door;
    private Window window;

    public Room(double size, char floorCode, Furniture furniture, Door door, Window window) {
        this.size = size;
        this.floorCode = floorCode;
        this.furniture = furniture;
        this.door = door;
        this.window = window;
    }

    public double getSize() {
        return size;
    }

    public char getFloorCode() {
        return floorCode;
    }

    public Door getDoor() {
        return door;
    }

    public Window getWindow() {
        return window;
    }

    public Furniture getFurniture() {
        return this.furniture;
    }

    public String useInsidePrivateMethod(String title) {
        printSome(title);
        return getFurniture().getTitle();
    }

    private void printSome(String NewTitle){
        System.out.print("**********\n");
        furniture.setTitle(NewTitle);

    }

}
