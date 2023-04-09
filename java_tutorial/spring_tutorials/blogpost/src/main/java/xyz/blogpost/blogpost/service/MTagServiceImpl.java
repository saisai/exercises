package xyz.blogpost.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import xyz.blogpost.blogpost.model.manytomany.MTag;
import xyz.blogpost.blogpost.repository.MTagRepository;

@Repository
public class MTagServiceImpl implements  MTagService{
    @Autowired
    MTagRepository mTagRepository;

    @Override
    public void save(MTag mTag) {
        mTagRepository.save(mTag);
    }

    @Override
    public void deleteAllInBatch() {
        mTagRepository.deleteAllInBatch();
    }
}
