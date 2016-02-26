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

    public InfToSupProcessor(){
        this.replaceThis = BinaryOperatorKind.LT;
        this.byThis = BinaryOperatorKind.GT;
    }
}