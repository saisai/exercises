package xyz.blogpost.blogpost.model.onetoone;

import javax.persistence.*;

@Entity
@Table(name="restaurant")
public class Restaurant {

    @Id
    //@GeneratedValue(strategy = GenerationType.AUTO)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private boolean servesHotDogs;
    private boolean servesPizza;

//    @OneToOne(mappedBy = "restaurant")
//    private Place place;

    @OneToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "place_id", nullable = false)
    private Place place;

    public Restaurant() {

    }

    public Restaurant(boolean servesHotDogs, boolean servesPizza) {
        this.servesHotDogs = servesHotDogs;
        this.servesPizza = servesPizza;
    }

    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public boolean isServesHotDogs() {
        return servesHotDogs;
    }

    public void setServesHotDogs(boolean servesHotDogs) {
        this.servesHotDogs = servesHotDogs;
    }

    public boolean isServesPizza() {
        return servesPizza;
    }

    public void setServesPizza(boolean servesPizza) {
        this.servesPizza = servesPizza;
    }

    @Override
    public String toString() {
        return "Restaurant{" +
                "id=" + id +
                ", servesHotDogs=" + servesHotDogs +
                ", servesPizza=" + servesPizza +
                '}';
    }
}
