package fr.polytech.devops.g1.stataspoon.processors.operators.binary;

import fr.polytech.devops.g1.stataspoon.selectors.selectors.ISelector;
import fr.polytech.devops.g1.stataspoon.selectors.SelectorController;
import spoon.processing.AbstractProcessor;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;

/**
 * Processor Model.
 *
 * @author Antoine Rollin
 */
public abstract class ProcessorModel extends AbstractProcessor<CtBinaryOperator> {

    protected BinaryOperatorKind replaceThis;
    protected BinaryOperatorKind byThis;
    private ISelector selector;


    protected ProcessorModel(BinaryOperatorKind replaceThis, BinaryOperatorKind byThis){
        this.replaceThis = replaceThis;
        this.byThis = byThis;
        this.selector = SelectorController.getInstance().getSelector();

    }

    @Override
    public void process(CtBinaryOperator op) {
        if(selector.isSelected(op)){
            // Find
            if (!op.getKind().equals(replaceThis)) return;

            // Replace
            op.setKind(byThis);
        }
    }
}