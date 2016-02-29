package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

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

    protected ProcessorModel(BinaryOperatorKind replaceThis, BinaryOperatorKind byThis){
        this.replaceThis = replaceThis;
        this.byThis = byThis;
    }

    @Override
    public void process(CtBinaryOperator operator) {
        // Find
        if (!operator.getKind().equals(replaceThis)) return;

        // Replace
        operator.setKind(byThis);
    }
}