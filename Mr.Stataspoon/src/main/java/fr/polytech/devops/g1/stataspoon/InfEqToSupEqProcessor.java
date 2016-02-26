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

    public InfEqToSupEqProcessor(){
        this.replaceThis = BinaryOperatorKind.LE;
        this.byThis = BinaryOperatorKind.GE;
    }
}