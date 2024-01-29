package club.snp.jobsapply;

import club.snp.jobsapply.entity.ERole;
import club.snp.jobsapply.entity.Role;
import club.snp.jobsapply.repository.RoleRepository;
import club.snp.jobsapply.service.FilesStorageService;
import jakarta.annotation.Resource;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class JobsapplyApplication {

	@Resource
	FilesStorageService storageService;
	public static void main(String[] args) {
		SpringApplication.run(JobsapplyApplication.class, args);
	}

	@Bean
	CommandLineRunner startUp(FilesStorageService storageService) {
		return args -> {
			storageService.init();
		};

	}
//	@Bean
//	CommandLineRunner startUp(RoleRepository roleRepository){
//		return args -> {
//			roleRepository.save(new Role(ERole.ROLE_USER));
//			roleRepository.save(new Role(ERole.ROLE_ADMIN));
//			roleRepository.save(new Role(ERole.ROLE_MODERATOR));
//		};
//	}

}
