package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Mutates & to |.
 *
 * @author Antoine Rollin
 */
public class AndToOrProcessor extends ProcessorModel {
    public AndToOrProcessor() {
        super(BinaryOperatorKind.AND, BinaryOperatorKind.OR);
    }
}