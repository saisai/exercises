package xyz.blogpost.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.model.manytomany.MTag;

@Repository
public interface MTagRepository extends JpaRepository<MTag, Long> {

    void deleteAllInBatch();
}
