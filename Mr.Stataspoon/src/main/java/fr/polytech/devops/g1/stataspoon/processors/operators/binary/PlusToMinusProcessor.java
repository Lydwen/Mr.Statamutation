package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Mutates plus to minus.
 *
 * @author Kevin Buisson
 */
public class PlusToMinusProcessor extends ProcessorModel {
    public PlusToMinusProcessor() {
        super(BinaryOperatorKind.PLUS, BinaryOperatorKind.MINUS);
    }
}