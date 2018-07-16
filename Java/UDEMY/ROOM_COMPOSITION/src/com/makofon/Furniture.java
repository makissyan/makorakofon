package com.makofon;

public class Furniture {

    private String title;
    private String material;
    private double size;

    public Furniture (String title, String material, double size){
        this.title = title;
        this.material = material;
        this.size = size;

    }

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title){
        this.title = title;
    }
}
