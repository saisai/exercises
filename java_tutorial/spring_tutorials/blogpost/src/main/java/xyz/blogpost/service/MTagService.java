package xyz.blogpost.service;

import xyz.blogpost.model.manytomany.MTag;

public interface MTagService {
    void save(MTag mTag);
    void deleteAllInBatch();
}
