package xyz.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import xyz.blogpost.model.onetomany.Comment;
import xyz.blogpost.repository.CommentRepository;

import java.util.Optional;

public class CommentServiceImpl implements CommentService{
    @Autowired
    CommentRepository commentRepository;

    @Override
    public Page<Comment> findByPostId(Long postId, Pageable pageable) {
        return commentRepository.findByPostId(postId, pageable);
    }

    @Override
    public Optional<Comment> findByIdAndPostId(Long id, Long postId) {
        return commentRepository.findByIdAndPostId(id, postId);
    }
}
