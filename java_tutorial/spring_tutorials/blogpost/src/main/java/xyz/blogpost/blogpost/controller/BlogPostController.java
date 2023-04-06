package xyz.blogpost.blogpost.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import xyz.blogpost.blogpost.model.BlogPost;
import xyz.blogpost.blogpost.service.BlogPostService;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@Controller
public class BlogPostController {

    private final Logger LOG = LoggerFactory.getLogger(BlogPostController.class);

//    private final BlogPostService blogPostService;
//    public BlogPostController(BlogPostService blogPostService) {
//        this.blogPostService = blogPostService;
//    }

    @Autowired
    BlogPostService blogPostService;


    @GetMapping(value="/")
    public String index(Model model) {
        return "index";
    }

    @GetMapping(value="/blogpost")
    public ModelAndView showBlogPosts() {
        List<BlogPost> blogPosts = blogPostService.findAll();

        Map<String, Object> params = new HashMap<String, Object>();
        params.put("blogPosts", blogPosts);

        return new ModelAndView("blogpost", params);

    }

    @RequestMapping(value = "/blogpost/{id}", method = RequestMethod.GET)
    public String deletePost(@PathVariable Long id) {
        LOG.info("Delete {} ", id);
        blogPostService.delete(id);
        return "redirect:/blogpost";

    }

    @RequestMapping(value = "/blogpost/update/{id}", method=RequestMethod.GET)
    public String updatePost(@PathVariable Long id, Model model) {
        LOG.info("Update {}", id);
        Optional<BlogPost> blogPost = blogPostService.findById(id);
        LOG.info("Exitsts {}", blogPost.get());
        model.addAttribute("blogpost", blogPost);
        return "update";
        //return "redirect:/blogpost/update";
    }

//    @DeleteMapping(value = "/blogpost/{id}")
//    public ResponseEntity<Long> deletePost(@PathVariable Long id) {
//
//        blogPostService.delete(id);
//
//        if (!isRemoved) {
//            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
//        }
//
//        return new ResponseEntity<>(id, HttpStatus.OK);
//    }

}
