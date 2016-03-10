package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import fr.polytech.devops.g1.stataspoon.processors.selectors.ISelector;
import fr.polytech.devops.g1.stataspoon.processors.selectors.SelectorController;
import fr.polytech.devops.g1.stataspoon.processors.selectors.SelectorPercentClasses;
import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;
import spoon.reflect.declaration.CtClass;

/**
 * Processor Model.
 *
 * @author Tom Dall'Agnol
 */
public class ProcessorCtClassPlusToMinus extends AbstractProcessor<CtBinaryOperator> {

    private BinaryOperatorKind inf;
    private BinaryOperatorKind sup;
    private ISelector selector;

    public ProcessorCtClassPlusToMinus(){
        this.inf = BinaryOperatorKind.LT;
        this.sup = BinaryOperatorKind.GT;
        this.selector = SelectorController.getInstance().getSelector();
    }

    @Override
    public void process(CtBinaryOperator op) {
        CtClass parent = op.getParent(CtClass.class);
        if(selector.isSelected(parent.getQualifiedName())){
            // Find
            if (!op.getKind().equals(inf)) return;

            // Replace
            op.setKind(sup);
        }
    }
}