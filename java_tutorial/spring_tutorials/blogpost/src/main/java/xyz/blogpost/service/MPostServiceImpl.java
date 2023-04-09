package xyz.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import xyz.blogpost.model.manytomany.MPost;
import xyz.blogpost.repository.MPostRepository;

@Service
public class MPostServiceImpl implements MPostService{
    @Autowired
    MPostRepository mPostRepository;

    @Override
    public void save(MPost mPost) {
        mPostRepository.save(mPost);
    }

    @Override
    public void deleteAllInBatch() {
        mPostRepository.deleteAllInBatch();
    }
}
