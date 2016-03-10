package fr.polytech.devops.g1.stataspoon.processors.selectors;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class SelectorPercentClasses implements ISelector {
    Map<String, Boolean> processedClasses;
    private Random r;
    private double percent;
    private static ISelector _instance;

    private SelectorPercentClasses(){
        processedClasses = new HashMap<>();
        r = new Random();
        this.percent = 0.2;
    }

    public static ISelector getInstance(){
        if(_instance == null){
            _instance = new SelectorPercentClasses();
        }
        return _instance;
    }

    public boolean isSelected(String className){
        if (processedClasses.containsKey(className)) {
            return processedClasses.get(className);
        }

        boolean willBeSelected = false;
        if(r.nextDouble()<=percent){
            willBeSelected = true;
        }
        this.processedClasses.put(className, willBeSelected);
        return willBeSelected;
    }
}
