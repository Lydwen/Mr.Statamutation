package fr.polytech.devops.g1.stataspoon;

import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Mutates equal to inequal.
 *
 * @author Antoine Rollin
 */
public class EqToIneqProcessor extends ProcessorModel {

    public EqToIneqProcessor(){
        this.replaceThis = BinaryOperatorKind.EQ;
        this.byThis = BinaryOperatorKind.NE;
    }

}