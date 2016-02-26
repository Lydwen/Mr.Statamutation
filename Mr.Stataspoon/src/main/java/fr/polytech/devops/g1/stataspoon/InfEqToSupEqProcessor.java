package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates indferior or equal to superior or equal.
 *
 * @author Antoine Rollin
 */
public class InfEqToSupEqProcessor extends ProcessorModel {

    @Override
    public void process(CtBinaryOperator operator) {
        // Mutate only + operator
        if (!operator.getKind().equals(BinaryOperatorKind.LE)) return;

        // Change it to - operator
        operator.setKind(BinaryOperatorKind.GE);
    }
}