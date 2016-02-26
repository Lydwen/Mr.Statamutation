package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates & to |.
 *
 * @author Antoine Rollin
 */
public class AndToORProcessor extends ProcessorModel {

    public AndToORProcessor(){
        this.replaceThis = BinaryOperatorKind.AND;
        this.byThis = BinaryOperatorKind.OR;
    }

}