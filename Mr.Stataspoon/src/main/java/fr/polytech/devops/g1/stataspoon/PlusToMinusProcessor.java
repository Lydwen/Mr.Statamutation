package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates plus to minus.
 *
 * @author Kevin Buisson
 */
public class PlusToMinusProcessor extends ProcessorModel {
    public PlusToMinusProcessor(){
        this.replaceThis = BinaryOperatorKind.PLUS;
        this.byThis = BinaryOperatorKind.MINUS;
    }
}