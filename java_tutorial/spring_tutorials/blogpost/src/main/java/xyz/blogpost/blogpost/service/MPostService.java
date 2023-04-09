package xyz.blogpost.blogpost.service;

import xyz.blogpost.blogpost.model.manytomany.MPost;

public interface MPostService {
    void save(MPost mPost);
    void deleteAllInBatch();
}
