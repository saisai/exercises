//package xyz.blogpost.controller;
//
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
//import org.springframework.ui.Model;
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.PostMapping;
//import xyz.blogpost.model.User;
//import xyz.blogpost.repository.UserRepository;
//
//import java.util.List;
//
//public class UserController {
//    @Autowired
//    private UserRepository userRepo;
//
////    @GetMapping("")
////    public String viewHomePage() {
////        return "index";
////    }
//
//    @GetMapping("/register")
//    public String showRegistrationForm(Model model) {
//        model.addAttribute("user", new User());
//
//        return "signup_form";
//    }
//
//    @PostMapping("/process_register")
//    public String processRegister(User user) {
//        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
//        String encodedPassword = passwordEncoder.encode(user.getPassword());
//        user.setPassword(encodedPassword);
//
//        userRepo.save(user);
//
//        return "register_success";
//    }
//
//    @GetMapping("/users")
//    public String listUsers(Model model) {
//        List<User> listUsers = userRepo.findAll();
//        model.addAttribute("listUsers", listUsers);
//
//        return "users";
//    }
//}
