package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates equal to inequal.
 *
 * @author Antoine Rollin
 */
public class EqToIneqProcessor extends ProcessorModel {

    @Override
    public void process(CtBinaryOperator operator) {
        // Mutate only = operator
        if (!operator.getKind().equals(BinaryOperatorKind.EQ)) return;

        // Change it to != operator
        operator.setKind(BinaryOperatorKind.NE);
    }
}