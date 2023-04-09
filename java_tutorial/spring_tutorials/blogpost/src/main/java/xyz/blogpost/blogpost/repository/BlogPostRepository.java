package xyz.blogpost.blogpost.repository;

import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.blogpost.model.BlogPost;

import java.util.List;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.repository.PagingAndSortingRepository;

@Repository
public interface BlogPostRepository extends PagingAndSortingRepository<BlogPost, Long> {

//    List<BlogPost> findAll(int pageNumber, int rowPerPage);
//
//
//    Iterable<Object> findAll(Pageable sortedByLastUpdateDesc);
}
