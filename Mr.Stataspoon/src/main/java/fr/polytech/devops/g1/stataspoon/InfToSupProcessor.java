package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates indferior srict to superior strict.
 *
 * @author Antoine Rollin
 */
public class InfToSupProcessor extends ProcessorModel {

    @Override
    public void process(CtBinaryOperator operator) {
        // Mutate only < operator
        if (!operator.getKind().equals(BinaryOperatorKind.LT)) return;

        // Change it to > operator
        operator.setKind(BinaryOperatorKind.GT);
    }
}