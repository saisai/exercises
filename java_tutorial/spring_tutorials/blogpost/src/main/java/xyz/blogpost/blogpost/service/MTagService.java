package xyz.blogpost.blogpost.service;

import xyz.blogpost.blogpost.model.manytomany.MTag;

public interface MTagService {
    void save(MTag mTag);
    void deleteAllInBatch();
}
