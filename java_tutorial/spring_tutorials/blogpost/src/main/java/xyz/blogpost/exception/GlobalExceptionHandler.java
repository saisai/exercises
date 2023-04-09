package xyz.blogpost.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.multipart.MaxUploadSizeExceededException;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;
import xyz.blogpost.message.ResponseMessage;


@ControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(MaxUploadSizeExceededException.class)
    public ResponseEntity<ResponseMessage> handleMaxSizeException(MaxUploadSizeExceededException exc) {
        return ResponseEntity.status(HttpStatus.EXPECTATION_FAILED).body(new ResponseMessage("File too large!"));
    }
}
//
//@ControllerAdvice
//public class GlobalExceptionHandler {
//    //https://jira.spring.io/browse/SPR-14651
//    //Spring 4.3.5 supports RedirectAttributes
//    @ExceptionHandler(MultipartException.class)
//    public String handleError1(MultipartException e, RedirectAttributes redirectAttributes) {
//
//        redirectAttributes.addFlashAttribute("message", e.getCause().getMessage());
//        return "redirect:/uploadStatus";
//
//    }
//
//    /* Spring < 4.3.5
//	@ExceptionHandler(MultipartException.class)
//    public String handleError2(MultipartException e) {
//
//        return "redirect:/errorPage";
//
//    }*/
//}
