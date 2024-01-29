package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.File;
import club.snp.jobsapply.entity.Position;
import club.snp.jobsapply.exception.ResourceNotFoundException;
import club.snp.jobsapply.service.FileService;
import club.snp.jobsapply.service.FilesStorageService;
import club.snp.jobsapply.service.PositionService;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:5173", maxAge = 3600)
@RestController
public class FileController {
    FileService fileService;
    PositionService positionService;

    FilesStorageService filesStorageService;

    FileController(FileService fileService,
                   PositionService positionService,
                   FilesStorageService filesStorageService) {

        this.fileService = fileService;
        this.positionService = positionService;
        this.filesStorageService = filesStorageService;
    }

    @GetMapping(value="/file")
    public List getFile() {
        return fileService.getAll();
    }
//    @PostMapping(value="/file",
//            consumes = {MediaType.MULTIPART_FORM_DATA_VALUE},
//            produces = {MediaType.APPLICATION_JSON_VALUE})
//    public String hello(@RequestParam("file") MultipartFile file) {
//        System.out.println("hello  test");
//        System.out.println(file.getOriginalFilename());
//        return "Hello";
//
//    }


    @PostMapping(value="/file",
            consumes = {MediaType.MULTIPART_FORM_DATA_VALUE},
            produces = {MediaType.APPLICATION_JSON_VALUE})
    public ResponseEntity<Object> createFiletest(@RequestParam(value = "title", required = false) String title,
                                 @RequestParam(value = "id", required = false) long positionID,
                                                 @RequestParam ("file") MultipartFile fileUploaded) throws IOException {


        Optional<File> searchData = fileService.findByTitle(title);

        if(searchData.isPresent()) {
            Map<String, Object> map = new HashMap<>();
            map.put("message", "Already exites");
            return new ResponseEntity<>(map, HttpStatus.OK);
        }

        try {

            String message = "";
            try {
                filesStorageService.save(fileUploaded);

                message = "Uploaded the file successfully: " + fileUploaded.getOriginalFilename();
//                return ResponseEntity.status(HttpStatus.OK).body(message);

                File _file = positionService.findById(positionID).map(position -> {
                    File newFile = new File(title);
                    newFile.setPosition(position);
                    return fileService.save(newFile);
                }).orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial with id = " + positionID));
                return new ResponseEntity<>(_file, HttpStatus.CREATED);

            } catch (Exception e) {
                message = "Could not upload the file: " + fileUploaded.getOriginalFilename() + ". Error: " + e.getMessage();
                return ResponseEntity.status(HttpStatus.EXPECTATION_FAILED).body(message);
            }


        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }

    }

    public ResponseEntity<Object> createFiletestgg(@RequestBody File file,
                                             @RequestParam ("file") MultipartFile fileUploaded) throws IOException {
        System.out.println("Hello world");
        System.out.println("fileUploaded " + fileUploaded.getOriginalFilename());
        System.out.println(file.getTitle());
        System.out.println("id " + file.getId());
        Optional<File> searchData = fileService.findByTitle(file.getTitle());
        System.out.println("apply.getTitle() " + file.getTitle());
        if(searchData.isPresent()) {
            Map<String, Object> map = new HashMap<>();
            map.put("message", "Already exites");
            return new ResponseEntity<>(map, HttpStatus.OK);
        }

        try {
            File _file = positionService.findById(file.getId()).map(position -> {
                file.setPosition(position);
                return fileService.save(file);
            }).orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial with id = " + file.getId()));
            return new ResponseEntity<>(_file, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping("/file/{id}")
    public ResponseEntity<HttpStatus> deleteFile(@PathVariable("id") long id) {
        try {
            fileService.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
