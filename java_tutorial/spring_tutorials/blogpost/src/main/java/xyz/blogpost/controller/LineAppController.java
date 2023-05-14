package xyz.blogpost.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class LineAppController {
    @GetMapping(value="/line")
    public ModelAndView index() {
        System.out.println("line");
        return new ModelAndView("line");
    }
}
