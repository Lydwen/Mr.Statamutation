package fr.polytech.devops.g1.stataspoon.selectors.selectors;

import spoon.reflect.declaration.CtElement;

import java.util.Random;

/**
 * Created by user on 10/03/16.
 */
public class SelectorPercentOfAll implements ISelector{
    private Random r;
    private double percent;

    public SelectorPercentOfAll(){
        this(0.2);
    }

    public SelectorPercentOfAll(double percent){
        this.percent = percent;
        r = new Random();
    }

    public boolean isSelected(CtElement element){
        if(r.nextDouble()<= percent){
            return true;
        }
        return false;
    }
}
