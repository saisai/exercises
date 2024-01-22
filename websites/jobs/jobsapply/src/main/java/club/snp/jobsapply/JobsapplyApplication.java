package club.snp.jobsapply;

import club.snp.jobsapply.entity.ERole;
import club.snp.jobsapply.entity.Role;
import club.snp.jobsapply.repository.RoleRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class JobsapplyApplication {
	public static void main(String[] args) {
		SpringApplication.run(JobsapplyApplication.class, args);
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
