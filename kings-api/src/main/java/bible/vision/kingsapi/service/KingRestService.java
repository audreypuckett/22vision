package bible.vision.kingsapi.service;

import bible.vision.kingsapi.data.JudahKings;
import bible.vision.kingsapi.exception.KingNotFoundException;
import bible.vision.kingsapi.model.King;
import bible.vision.kingsapi.repository.KingJPARepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class KingRestService {
    List<King> kingsOfJudah = JudahKings.getKings();
    private KingJPARepository repository;

    public KingRestService(KingJPARepository repository) {
        this.repository = repository;
        for (King k : kingsOfJudah) {
            System.out.println(k);
        }
    }

    public King findById(int id) throws KingNotFoundException {
        return repository.findById(id)
                .orElseThrow(() -> new KingNotFoundException("King with id: " + id + " was not found"));    }
}
