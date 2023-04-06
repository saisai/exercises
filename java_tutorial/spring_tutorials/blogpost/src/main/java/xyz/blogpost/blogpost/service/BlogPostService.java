package xyz.blogpost.blogpost.service;

import xyz.blogpost.blogpost.model.BlogPost;

import java.util.List;
import java.util.Optional;

public interface BlogPostService {

    public List<BlogPost> findAll();

    void delete(Long id);

    public Optional<BlogPost> findById(Long id);
}
