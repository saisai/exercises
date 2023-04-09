package xyz.blogpost.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.model.manytomany.MPost;

@Repository
public interface MPostRepository extends JpaRepository<MPost, Long> {

    void deleteAllInBatch();
}
