package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;

/**
 * Processor Model.
 *
 * @author Tom Dall'Agnol
 */
public class ProcessorCtClassPlusToMinus extends ProcessorModel {

    public ProcessorCtClassPlusToMinus() {
        super(BinaryOperatorKind.LT, BinaryOperatorKind.GT);

    }
}