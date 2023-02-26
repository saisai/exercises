package com.zetcode.app.json;

import java.util.Objects;

public class User {

    private String name;
    private String occupation;
    private int siblings;
    private double height;
    private boolean married;

    public User(String name, String occupation, int siblings, double height, boolean married) {
        this.name = name;
        this.occupation = occupation;
        this.siblings = siblings;
        this.height = height;
        this.married = married;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }

    public int getSiblings() {
        return siblings;
    }

    public void setSiblings(int siblings) {
        this.siblings = siblings;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public boolean isMarried() {
        return married;
    }

    public void setMarried(boolean married) {
        this.married = married;
    }
    @Override
    public boolean equals(Object o) {
        if(this == o) return true;
        if(o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return siblings == user.siblings && Double.compare(user.height, height) == 0 &&
                married == user.married && Objects.equals(name, user.name)
                && Objects.equals(occupation, user.occupation);
    }

    @Override
    public  int hashCode() {
        return Objects.hash(name, occupation, siblings, height, married);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("User{");
        sb.append("name='").append(name).append('\'');
        sb.append(", occupation='").append(occupation).append('\'');
        sb.append(", siblings=").append(siblings);
        sb.append(", height=").append(height);
        sb.append(", married=").append(married);
        sb.append('}');
        return sb.toString();
    }


}
