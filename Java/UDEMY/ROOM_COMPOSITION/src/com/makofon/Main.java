package com.makofon;

public class Main {

    public static void main(String[] args) {
        Furniture table = new Furniture("TableToDisplay\n","Wood",3.5);
        Door door = new Door("Glass",2);
        Window myWindow = new Window(2,'W');

        Room myRoom = new Room(1,'A',table,door,myWindow);

        System.out.print(myRoom.getFurniture().getTitle());

        System.out.print(myRoom.useInsidePrivateMethod("BIG BLACK TABLE"));

    }
}
