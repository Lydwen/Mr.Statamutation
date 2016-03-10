package fr.polytech.devops.g1.stataspoon.selectors.selectors;

import spoon.reflect.declaration.CtElement;

/**
 * This selector select every element
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class SelectorAll implements ISelector{

    public boolean isSelected(CtElement element){
        return true;
    }
}
