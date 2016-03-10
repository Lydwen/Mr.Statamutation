package fr.polytech.devops.g1.stataspoon.selectors;

import fr.polytech.devops.g1.stataspoon.selectors.factory.*;

/**
 * Created by user on 10/03/16.
 */
public enum Selectors {
    PERCENTOFCLASSES("percent of classes", new FactorySelectorPercentOfClasses()),
    PERCENTOFALL("percent of all", new FactorySelectorPercentOfAll()),
    ALLRANDOM("random", new FactoryAllRandom()),
    ALL("all", new FactoryIdentitySelectorAll());

    private String name;
    private FactorySelector factory;

    Selectors(String name, FactorySelector factory){
        this.name = name;
        this.factory = factory;
    }

    public static FactorySelector getFactory(String name){
        for(Selectors s : Selectors.values()){
            if(s.getName().equals(name)) {
                return s.getFactory();
            }
        }
        return null;
    }

    public static boolean isSelector(String name){
        for(Selectors s : Selectors.values()){
            if(s.getName().equals(name))
                return true;
        }
        return false;
    }

    public FactorySelector getFactory(){
        return this.factory;
    }

    public String getName(){
        return this.name;
    }
}
