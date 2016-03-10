package fr.polytech.devops.g1.stataspoon.selectors.selectors;

import spoon.reflect.declaration.CtElement;

/**
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public interface ISelector {
    boolean isSelected(CtElement element);
}
