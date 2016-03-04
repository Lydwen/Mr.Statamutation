package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;
import spoon.reflect.declaration.CtMethod;

/**
 * Mutates inferior or equal to superior or equal.
 *
 * @author Antoine Rollin
 */
public class InfEqToSupEqProcessor extends ProcessorModel {
    public InfEqToSupEqProcessor() {
        super(BinaryOperatorKind.LE, BinaryOperatorKind.GE);
    }

    public void process(CtBinaryOperator operator){
        // Find
        if (!operator.getKind().equals(replaceThis)) return;

        CtMethod parent = operator.getParent(CtMethod.class);
        if (parent!=null && !parent.getSimpleName().equals("infeq2")) return;

        // Replace
        operator.setKind(byThis);
    }
}