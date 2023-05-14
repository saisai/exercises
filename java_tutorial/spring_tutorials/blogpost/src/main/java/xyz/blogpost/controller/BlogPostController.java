package xyz.blogpost.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import xyz.blogpost.model.BlogPost;
import xyz.blogpost.service.BlogPostService;
import xyz.blogpost.service.EmailAsyncService;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import java.util.*;

@Controller
public class BlogPostController {
    private final Logger LOG = LoggerFactory.getLogger(BlogPostController.class);

    private final int ROW_PER_PAGE = 3;

    @Autowired
    BlogPostService blogPostService;

    @Autowired
    private HttpServletRequest request;

    @Autowired
    EmailAsyncService emailAsyncService;

    @GetMapping(value="/")
    public String index(Model model) {
        //return "index";
        return "redirect:/blogpost";
    }

//    @GetMapping(value="/blogpost")
//    public ModelAndView showBlogPosts() {
//        List<BlogPost> blogPosts = blogPostService.findAll();
//        Map<String, Object> params = new HashMap<String, Object>();
//        params.put("blogPosts", blogPosts);
//        return new ModelAndView("blogpost", params);
//    }

//    @GetMapping(value = "/blogpost")
//    public String getBlogPosts(Model model,
//                           @RequestParam(value = "page", defaultValue = "1") int pageNumber) {
//        List<BlogPost> blogPosts = blogPostService.findAll(pageNumber, ROW_PER_PAGE);
//
//        long count = blogPostService.count();
//        boolean hasPrev = pageNumber > 1;
//        boolean hasNext = (pageNumber * ROW_PER_PAGE) < count;
//        model.addAttribute("blogPosts", blogPosts);
//        model.addAttribute("hasPrev", hasPrev);
//        model.addAttribute("prev", pageNumber - 1);
//        model.addAttribute("hasNext", hasNext);
//        model.addAttribute("next", pageNumber + 1);
//        return "blogpost";
//        //return "note-list";
//    }

    public void showRequestHeaders(HttpServletRequest request) {
        HttpServletRequest httpServletRequest = request;
        Enumeration<String> headerNames = request.getHeaderNames();

        LOG.info("Http Headers");

        if(headerNames != null) {
            while(headerNames.hasMoreElements()) {
                LOG.info("Header: {}", httpServletRequest.getHeader(headerNames.nextElement()));
            }
        }

    }

    //get user agent
    private String getUserAgent() {
        return request.getHeader("user-agent");
    }

    //get request headers
    private Map<String, String> getHeadersInfo() {

        Map<String, String> map = new HashMap<String, String>();

        Enumeration headerNames = request.getHeaderNames();
        while (headerNames.hasMoreElements()) {
            String key = (String) headerNames.nextElement();
            String value = request.getHeader(key);
            map.put(key, value);
        }

        return map;
    }


    //@GetMapping(value = {"/blogpost", "/"})
    @GetMapping(value = {"/blogpost"})
    public String posts(@RequestParam(value = "pageNumber", required = false, defaultValue = "1") int pageNumber,
                        @RequestParam(value = "size", required = false, defaultValue = "5") int size, Model model,
                        HttpServletRequest request) {
        LOG.info("Session Id {}", request.getSession().getId());

        showRequestHeaders(request);
        LOG.info("Headers {}", getHeadersInfo());

        model.addAttribute("blogPosts", blogPostService.getPage(pageNumber, size));
        return "blogpost";
    }

    @RequestMapping(value = "/blogpost/{id}", method = RequestMethod.GET)
    public String deletePost(@PathVariable Long id) {
        LOG.info("Delete {} ", id);
        blogPostService.delete(id);
        return "redirect:/blogpost";
    }

    @RequestMapping(value = "/blogpost/update/{id}", method=RequestMethod.GET)
    public ModelAndView updatePost(@PathVariable Long id, Model mode) {
        LOG.info("Update {}", id);
        Optional<BlogPost> blogPost = blogPostService.findById(id);
        LOG.info("Exitsts {}", blogPost.get());
        ModelAndView mav = new ModelAndView();
        mav.addObject("blogpost", blogPost.get());
        mav.setViewName("update");
        return mav;
    }

    @PostMapping(value="/blogpost/editedUpdate")
    public String editedUpdate(@ModelAttribute BlogPost blogPost) {
        LOG.info("edited Update {}", blogPost.getLink());
        Long id = Long.parseLong(String.valueOf(blogPost.getId()));
        Optional<BlogPost> blogPostResult = blogPostService.findById(id);
        Calendar calendar = Calendar.getInstance();
        Date date =  calendar.getTime();
        blogPost.setCreatedAt(blogPostResult.get().getCreatedAt());
        blogPost.setUpdatedAt(date);
        blogPostService.save(blogPost);
        return "redirect:/blogpost";
    }

    @GetMapping(value="/blogpost/addForm")
    public String addForm(){
        return "addBlogPostForm";
    }

    @PostMapping(value="/blogpost/add")
    //public String addBlogPost(@ModelAttribute @Valid BlogPost blogPost, BindingResult result,  Model model) {
    public String addBlogPost(@Valid BlogPost blogPost, BindingResult result,  Model model) {
        LOG.info("BlogPost {}", blogPost.toString());
        if(result.hasErrors()) {
            model.addAttribute("blogPost", blogPost);
            return "addBlogPostForm";
        }
        LOG.info("Add {}", blogPost.getLink());
        Calendar calendar = Calendar.getInstance();
        Date date =  calendar.getTime();
        blogPost.setCreatedAt(date);
        blogPostService.save(blogPost);
        return "redirect:/blogpost";
    }

    // ajax post
    @RequestMapping(value = "/blogpost/ajax", method = RequestMethod.POST)
    @ResponseBody
    public String sendPostMessage(@RequestParam("title") String title,
                                  @RequestParam("link") String link,
                                  @RequestParam("description") String description
                                  ) {

        LOG.info("description {}", description);
        Calendar calendar = Calendar.getInstance();
        Date date =  calendar.getTime();
        BlogPost blogPost = new BlogPost(title, link, description, date);
        //blogPost.setCreatedAt(date);
        blogPostService.save(blogPost);
        emailAsyncService.sendEmail();
        return "Success";

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
