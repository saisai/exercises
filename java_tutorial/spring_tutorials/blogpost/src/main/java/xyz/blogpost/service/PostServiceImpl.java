package xyz.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import xyz.blogpost.model.onetomany.Post;
import xyz.blogpost.repository.PostRepository;

@Service
public class PostServiceImpl implements PostService {

    @Autowired
    PostRepository postRepository;
    @Override
    public void save(Post post) {
        postRepository.save(post);
    }
}
