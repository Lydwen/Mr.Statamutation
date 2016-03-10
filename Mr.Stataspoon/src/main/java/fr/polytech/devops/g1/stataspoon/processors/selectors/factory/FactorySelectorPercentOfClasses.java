package fr.polytech.devops.g1.stataspoon.processors.selectors.factory;

import fr.polytech.devops.g1.stataspoon.processors.selectors.ISelector;
import fr.polytech.devops.g1.stataspoon.processors.selectors.SelectorPercentOfClasses;

import javax.xml.stream.XMLStreamReader;
import java.util.Map;

/**
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class FactorySelectorPercentOfClasses implements FactorySelector{

    public ISelector createSelector(Map<String,String> params){
        String percentString = params.get("percent");
        double percent = Double.valueOf(params.get("percent"));
        return new SelectorPercentOfClasses(percent/100);
    }
}
