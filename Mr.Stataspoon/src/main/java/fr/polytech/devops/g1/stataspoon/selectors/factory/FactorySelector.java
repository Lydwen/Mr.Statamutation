package fr.polytech.devops.g1.stataspoon.selectors.factory;

import fr.polytech.devops.g1.stataspoon.selectors.selectors.ISelector;

import java.util.Map;

/**
 * Created by user on 10/03/16.
 */
public interface FactorySelector {

    ISelector createSelector(Map<String, String> params);
}
