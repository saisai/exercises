package xyz.blogpost.blogpost.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.blogpost.model.onetoone.Place;

@Repository
public interface PlaceRepository extends JpaRepository<Place, Long> {
}
