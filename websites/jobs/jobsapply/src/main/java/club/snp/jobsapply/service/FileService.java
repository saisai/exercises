package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.File;
import club.snp.jobsapply.repository.FileRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class FileService {
    FileRepository fileRepository;

    FileService(FileRepository fileRepository) {
        this.fileRepository = fileRepository;
    }

    public List<File> getAll() {
        for(File obj : fileRepository.findAll()) {
            System.out.println("Test " + obj.getPosition() + " " + obj.getTitle());
        }
        return fileRepository.findAll();
    }

    public void deleteById(long id) {
        fileRepository.deleteById(id);
    }

    public Optional<File> findById(long id) {
        Optional<File> fileData = fileRepository.findById(id);
        return fileData;
    }

    public File save(File file) {
        fileRepository.save(file);
        return file;
    }

    public Optional<File> findByTitle(String title) {
        Optional<File> fileData = fileRepository.findByTitle(title);
        return fileData;
    }

}
