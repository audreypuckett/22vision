package bible.vision.kingsapi.controller;

import bible.vision.kingsapi.service.KingService;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KingRestController {
    private KingService service;

    public KingRestController(KingService service) {
        this.service = service;
    }
}
