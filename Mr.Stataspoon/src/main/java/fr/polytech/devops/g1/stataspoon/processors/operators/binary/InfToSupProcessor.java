package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Mutates indferior srict to superior strict.
 *
 * @author Antoine Rollin
 */
public class InfToSupProcessor extends ProcessorModel {
    public InfToSupProcessor() {
        super(BinaryOperatorKind.LT, BinaryOperatorKind.GT);
    }
}