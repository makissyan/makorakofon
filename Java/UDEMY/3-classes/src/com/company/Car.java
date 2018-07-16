package com.company;

public class Car {

    private int doors;
    private int windows;
    private String model;
    private String engine;
    private String color;

    public void setModel(String model) {
        String validModel = model.toLowerCase();
        if ((validModel.equals("carrera")) || (validModel.equals("cayenne")))
            this.model = model;
        else
            this.model = "unknown";
    }

    public String getModel() {
        return this.model;
    }
}
