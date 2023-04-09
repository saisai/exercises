package xyz.blogpost.model.onetoone;

import javax.persistence.*;
import java.util.Objects;

@Entity
@Table(name="place")
public class Place {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String address;

//    @OneToOne(cascade = CascadeType.ALL)
//    @JoinColumn(name = "restaurant_id", referencedColumnName = "id")
//    private Restaurant restaurant;

    @OneToOne(fetch = FetchType.LAZY,
            cascade =  CascadeType.ALL,
            mappedBy = "place")
    private Restaurant restaurant;


    public Place() {

    }

    public Place(String name, String address) {
        this.name = name;
        this.address = address;
    }

    public Restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(Restaurant restaurant) {
        this.restaurant = restaurant;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Place place = (Place) o;
        return Objects.equals(id, place.id) && Objects.equals(name, place.name) && Objects.equals(address, place.address);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, address);
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Place{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", address='" + address + '\'' +
                '}';
    }
}
