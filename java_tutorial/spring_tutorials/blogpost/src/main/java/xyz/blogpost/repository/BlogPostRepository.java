package xyz.blogpost.repository;

import io.lettuce.core.dynamic.annotation.Param;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import xyz.blogpost.model.BlogPost;

import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;

@Repository
public interface BlogPostRepository extends PagingAndSortingRepository<BlogPost, Long> {

    @Transactional
    @Modifying
    @Query("UPDATE BlogPost b set b.delete = 1 WHERE b.id = :id")
    void updateDelete(@Param("id") Long id);

    @Transactional
    @Modifying
    @Query("UPDATE BlogPost b set b.delete = 1 WHERE b.createdAt < :endTime")
    void deleteAll(@Param("endTime") Timestamp endTime);


//    @Query("select id, created_at, description, link, title from BlogPost b where b.createdAt between ?1 and ?2")
//    List<BlogPost> findAllByCreatedAtBetween(Date localDateTime, Date localDateTime2) ;

//    List<BlogPost> findAll(int pageNumber, int rowPerPage);
//
//
//    Iterable<Object> findAll(Pageable sortedByLastUpdateDesc);
}
