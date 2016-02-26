package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Processor Model.
 *
 * @author Antoine Rollin
 */
public abstract class ProcessorModel extends AbstractProcessor<CtBinaryOperator> {

    protected BinaryOperatorKind replaceThis;
    protected BinaryOperatorKind byThis;

    @Override
    public void process(CtBinaryOperator operator) {
        // Find
        if (!operator.getKind().equals(replaceThis)) return;

        // Replace
        operator.setKind(byThis);
    }
}