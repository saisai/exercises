package xyz.blogpost.model;

public class BlogPostCriteria {

    private Long blogPostID;
    private String endTime;

    public Long getBlogPostID() {
        return blogPostID;
    }

    public void setBlogPostID(Long blogPostID) {
        this.blogPostID = blogPostID;
    }

    public String getEndTime() {
        return endTime;
    }

    public void setEndTime(String endTime) {
        this.endTime = endTime;
    }
}
