package bible.vision.kingsapi.data;

import bible.vision.kingsapi.model.King;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class JudahKings {
    static List<IMakeKing> kingsToMake = new ArrayList<IMakeKing>(
            Arrays.asList(new David(), new Solomon())
    );

    public static List<King> getKings(){
       List<King> kings = makeKings();
       setPredecessors(kings);
       return kings;
    }

    private static List<King> makeKings(){
        List<King> kings = new ArrayList<>();
        for (IMakeKing kingToMake : kingsToMake){
            King king = kingToMake.makeKing();
            kings.add(king);
        }
        return kings;
    }

    private static void setPredecessors(List<King> kings){
        for(int i = 0; i < kings.size(); i++){
            int predecessor = i+1;
            if(predecessor< kings.size()) {
                kings.get(i).setPredecessor(kings.get((predecessor)));
            }
        }
    }

}
