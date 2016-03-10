package fr.polytech.devops.g1.stataspoon.selectors.selectors;

/**
 * Created by user on 10/03/16.
 */
public class SelectorAllRandom extends SelectorPercentOfAll {

    public SelectorAllRandom(){
        //50% chance of mutating. So it's "random"
        super(0.5);
    }
}
