package fr.polytech.devops.g1.stataspoon.selectors.factory;

import fr.polytech.devops.g1.stataspoon.selectors.selectors.ISelector;
import fr.polytech.devops.g1.stataspoon.selectors.selectors.SelectorAllRandom;

import java.util.Map;

/**
 * Created by user on 10/03/16.
 */
public class FactoryAllRandom implements FactorySelector {

    public ISelector createSelector(Map<String, String> params){
        return new SelectorAllRandom();
    }
}
