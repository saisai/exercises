package zengcode.medium.com.repository;

import org.springframework.data.repository.CrudRepository;
import zengcode.medium.com.model.Person;

import java.util.List;


public interface PersonRepository extends CrudRepository<Person, Long> {

    List<Person> findByFirstName(String name);
}
