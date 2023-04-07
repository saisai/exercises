package xyz.blogpost.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import xyz.blogpost.blogpost.model.BlogPost;
import xyz.blogpost.blogpost.repository.BlogPostRepository;

import java.util.List;
import java.util.Optional;

@Service
public class BlogPostServiceImpl implements BlogPostService{
    @Autowired
    BlogPostRepository blogPostRepository;

    @Override
    public List<BlogPost> findAll() {
        List<BlogPost> results = (List<BlogPost>) blogPostRepository.findAll();
        return results;
    }

    @Override
    public void delete(Long id) {
        blogPostRepository.deleteById(id);
    }

    @Override
    public Optional<BlogPost> findById(Long id) {
        return blogPostRepository.findById(id);
    }

    @Override
    public void save(BlogPost blogPost) {
        blogPostRepository.save(blogPost);
    }


}
