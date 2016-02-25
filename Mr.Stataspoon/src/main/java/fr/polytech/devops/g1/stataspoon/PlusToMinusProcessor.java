package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates plus to minus.
 *
 * @author Kevin Buisson
 */
public class PlusToMinusProcessor extends AbstractProcessor<CtBinaryOperator> {
    @Override
    public void process(CtBinaryOperator operator) {
        // Mutate only + operator
        if (!operator.getKind().equals(BinaryOperatorKind.PLUS)) return;

        // Change it to - operator
        operator.setKind(BinaryOperatorKind.MINUS);
    }
}