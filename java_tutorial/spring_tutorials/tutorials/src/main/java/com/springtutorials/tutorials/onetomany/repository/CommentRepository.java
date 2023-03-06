package com.springtutorials.tutorials.onetomany.repository;

import com.springtutorials.tutorials.onetomany.model.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

import javax.transaction.Transactional;
import java.util.List;

public interface CommentRepository extends JpaRepository<Comment, Long> {

    List<Comment> findByTutorials2_Id(long tutorials2_id);

    @Transactional
    void deleteByTutorials2_Id(long tutorials2_id);
}
