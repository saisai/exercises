package xyz.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import xyz.blogpost.model.BlogPost;
import xyz.blogpost.model.paging.Paged;
import xyz.blogpost.model.paging.Paging;
import xyz.blogpost.repository.BlogPostRepository;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;

import javax.persistence.criteria.CriteriaBuilder;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

@Service
public class BlogPostServiceImpl implements BlogPostService{
    @Autowired
    BlogPostRepository blogPostRepository;

    @Override
    public List<BlogPost> findAll(int pageNumber, int rowPerPage) {
        List<BlogPost> blogPosts = new ArrayList<>();
        Pageable sortedByLastUpdateDesc = PageRequest.of(pageNumber - 1, rowPerPage,
                Sort.by("updatedAt").descending());
        blogPostRepository.findAll(sortedByLastUpdateDesc).forEach(blogPosts::add);
        return blogPosts;

    }

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

    @Override
    public Long count() {
        return blogPostRepository.count();
    }

    @Override
    public Paged<BlogPost> getPage(int pageNumber, int size) {
        Sort sort = Sort.by("id");
        //sort = sort.ascending();
        sort = sort.descending();
        PageRequest request = PageRequest.of(pageNumber - 1, size, sort);
        Page<BlogPost> postPage = blogPostRepository.findAll(request);
        return new Paged<>(postPage, Paging.of(postPage.getTotalPages(), pageNumber, size));
    }


    public void updateDelete(Long id) {
        blogPostRepository.updateDelete(id);
    }

    public void deleteAll(Timestamp endTime) {
        blogPostRepository.deleteAll(endTime);
    }


//    public List<BlogPost> findByCreatedAtBetween(Date localDateTime, Date localDateTime2){
//        return blogPostRepository.findAllByCreatedAtBetween(localDateTime, localDateTime2);
//    }




}
