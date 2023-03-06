package com.springtutorials.tutorials.manytomany.repository;

import com.springtutorials.tutorials.manytomany.model.Tag;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TagRepository extends JpaRepository<Tag, Long> {
    List<Tag> findTagByTutorials3Id(Long tutorials3Id);

}
