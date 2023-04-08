package xyz.blogpost.blogpost.service;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import xyz.blogpost.blogpost.model.onetomany.Comment;

import java.util.Optional;

public interface CommentService {
    Page<Comment> findByPostId(Long postId, Pageable pageable);
    Optional<Comment> findByIdAndPostId(Long id, Long postId);
}
