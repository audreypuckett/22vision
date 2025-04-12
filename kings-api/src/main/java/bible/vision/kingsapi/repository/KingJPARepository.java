package bible.vision.kingsapi.repository;


import bible.vision.kingsapi.model.King;
import org.springframework.data.jpa.repository.JpaRepository;

public interface KingJPARepository extends JpaRepository<King, Integer> {
}
