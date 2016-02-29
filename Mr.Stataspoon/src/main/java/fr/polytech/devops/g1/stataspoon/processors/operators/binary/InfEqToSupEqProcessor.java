package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Mutates inferior or equal to superior or equal.
 *
 * @author Antoine Rollin
 */
public class InfEqToSupEqProcessor extends ProcessorModel {
    public InfEqToSupEqProcessor() {
        super(BinaryOperatorKind.LE, BinaryOperatorKind.GE);
    }
}