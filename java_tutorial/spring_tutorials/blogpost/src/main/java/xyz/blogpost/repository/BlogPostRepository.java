package xyz.blogpost.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.model.BlogPost;

@Repository
public interface BlogPostRepository extends PagingAndSortingRepository<BlogPost, Long> {

//    List<BlogPost> findAll(int pageNumber, int rowPerPage);
//
//
//    Iterable<Object> findAll(Pageable sortedByLastUpdateDesc);
}
