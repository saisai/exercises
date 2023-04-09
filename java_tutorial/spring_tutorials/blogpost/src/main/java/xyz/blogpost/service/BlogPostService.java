package xyz.blogpost.service;

import xyz.blogpost.model.BlogPost;
import xyz.blogpost.model.paging.Paged;

import java.util.List;
import java.util.Optional;

public interface BlogPostService {

    List<BlogPost> findAll(int pageNumber, int rowPerPage);

    public List<BlogPost> findAll();

    void delete(Long id);

    public Optional<BlogPost> findById(Long id);

    void save(BlogPost blogPost);

    Long count();

    Paged<BlogPost> getPage(int pageNumber, int size);
}
