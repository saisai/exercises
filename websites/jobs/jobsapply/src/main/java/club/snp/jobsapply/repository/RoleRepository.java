package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.ERole;
import club.snp.jobsapply.entity.Role;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface RoleRepository extends JpaRepository<Role, Long> {
    Optional<Role> findByName(ERole name);
}
