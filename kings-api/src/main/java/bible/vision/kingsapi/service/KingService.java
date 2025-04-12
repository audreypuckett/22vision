package bible.vision.kingsapi.service;

import bible.vision.kingsapi.exception.KingNotFoundException;
import bible.vision.kingsapi.model.King;
import bible.vision.kingsapi.repository.KingJPARepository;
import org.springframework.stereotype.Service;

@Service
public class KingService {

    private KingJPARepository repository;
    private KingRestService restService;

    public KingService(KingJPARepository repository, KingRestService restService) {
        this.repository = repository;
        this.restService = restService;
    }

    private King save(King king) {
        return repository.save(king);
    }

    private King findById(int id) {
        King foundKing;
        try{
            foundKing = restService.findById(id);
        } catch (KingNotFoundException e){
            System.out.println(e.getMessage());
            foundKing = null;
        }
        return foundKing;
    }

}
