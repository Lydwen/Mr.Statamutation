package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Mutates equal to inequal.
 *
 * @author Antoine Rollin
 */
public class EqToIneqProcessor extends ProcessorModel {
    public EqToIneqProcessor() {
        super(BinaryOperatorKind.EQ, BinaryOperatorKind.NE);
    }
}