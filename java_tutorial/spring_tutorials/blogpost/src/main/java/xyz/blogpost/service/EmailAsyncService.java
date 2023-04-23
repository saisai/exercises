package xyz.blogpost.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class EmailAsyncService {

    private static final Logger Log = LoggerFactory.getLogger(EmailAsyncService.class);

//    @Autowired
//    private MailService mailService;

    @Async
    public void sendEmail() {
        Log.info("sending email now...");
    }
//    public void sendEmail(User user, String email) {
//        if (!user.getEmail().equals(email)) {
//            user.setEmailTemp(email);
//            Map map = new HashMap();
//            map.put("name", user.getName() + " " + user.getSurname());
//            map.put("url", "http://activationLink");
//            mailService.sendMail(map, "email-activation");
//        }
//    }
}
