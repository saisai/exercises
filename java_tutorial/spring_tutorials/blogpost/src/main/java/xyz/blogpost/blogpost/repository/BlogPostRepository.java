package xyz.blogpost.blogpost.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.blogpost.model.BlogPost;

@Repository
public interface BlogPostRepository extends CrudRepository<BlogPost, Long> {
}
