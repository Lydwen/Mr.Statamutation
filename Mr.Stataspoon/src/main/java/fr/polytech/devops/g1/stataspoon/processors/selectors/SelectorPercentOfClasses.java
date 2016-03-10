package fr.polytech.devops.g1.stataspoon.processors.selectors;

import spoon.reflect.declaration.CtClass;
import spoon.reflect.declaration.CtElement;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * Selector that permits to mutate
 * only a certain percentage of the classes
 *
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class SelectorPercentOfClasses implements ISelector {
    Map<String, Boolean> processedClasses;
    private Random r;
    private double percent;

    public SelectorPercentOfClasses(){
        this(0.2);
    }

    public SelectorPercentOfClasses(double percent){
        processedClasses = new HashMap<>();
        r = new Random();
        this.percent = percent;
    }

    @Override
    public boolean isSelected(CtElement element){
        CtClass parent = element.getParent(CtClass.class);
        boolean willBeSelected = false;

        if(parent != null) {
            String className = parent.getQualifiedName();

            if (processedClasses.containsKey(className)) {
                willBeSelected = processedClasses.get(className);
            }else {
                if (r.nextDouble() <= percent) {
                    willBeSelected = true;
                }
                this.processedClasses.put(className, willBeSelected);
            }
        }
        return willBeSelected;

    }
}
