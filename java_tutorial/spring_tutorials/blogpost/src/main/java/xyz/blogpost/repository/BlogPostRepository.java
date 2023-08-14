package xyz.blogpost.repository;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;
import xyz.blogpost.model.BlogPost;

import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;

@Repository
public interface BlogPostRepository extends PagingAndSortingRepository<BlogPost, Long> {

//    @Query("select id, created_at, description, link, title from BlogPost b where b.createdAt between ?1 and ?2")
//    List<BlogPost> findAllByCreatedAtBetween(Date localDateTime, Date localDateTime2) ;

//    List<BlogPost> findAll(int pageNumber, int rowPerPage);
//
//
//    Iterable<Object> findAll(Pageable sortedByLastUpdateDesc);
}
