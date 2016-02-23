package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtClass;

/**
 * NeutralProcessor, does nothing, just for build chain testing.
 *
 * @author Kévin Buisson
 */
public class NeutralProcessor extends AbstractProcessor<CtClass<?>> {
    public void process(CtClass<?> ctClass) {
        // Do nothing
    }
}