package fr.polytech.devops.g1.stataspoon.selectors.factory;

import fr.polytech.devops.g1.stataspoon.selectors.selectors.ISelector;
import fr.polytech.devops.g1.stataspoon.selectors.selectors.SelectorPercentOfAll;

import java.util.Map;

/**
 * Created by user on 10/03/16.
 */
public class FactorySelectorPercentOfAll implements FactorySelector {

    public ISelector createSelector(Map<String,String> params){
        String percentString = params.get("percent");
        double percent = Double.valueOf(params.get("percent"));
        return new SelectorPercentOfAll(percent/100);
    }
}
