package fr.polytech.devops.g1.stataspoon.processors.selectors;

/**
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class SelectorController {

    private static SelectorController _instance;


    public static SelectorController getInstance(){
        if (_instance == null){
            _instance = new SelectorController();
        }
        return _instance;
    }

    public ISelector getSelector(){
        return SelectorPercentClasses.getInstance();
    }

}
