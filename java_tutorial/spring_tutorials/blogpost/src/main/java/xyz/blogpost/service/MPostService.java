package xyz.blogpost.service;

import xyz.blogpost.model.manytomany.MPost;

public interface MPostService {
    void save(MPost mPost);
    void deleteAllInBatch();
}
