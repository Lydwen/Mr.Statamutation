package fr.polytech.devops.g1.stataspoon.processors.selectors;

import fr.polytech.devops.g1.stataspoon.processors.selectors.factory.FactorySelector;

import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;
import javax.xml.stream.events.XMLEvent;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Tom Dall'Agnol on 10/03/16.
 */
public class SelectorController {
    private ISelector selector;
    private static SelectorController _instance;

    private SelectorController(){
        System.out.println("COUCOU=================================================");
        selector = new SelectorPercentOfClasses();
        XMLInputFactory xmlif = XMLInputFactory.newInstance();
        try {
            XMLStreamReader xmlsr = xmlif.createXMLStreamReader(new FileReader("poir.xml"));
            int eventType;
            while(xmlsr.hasNext()){
                eventType = xmlsr.next();
                if(eventType== XMLEvent.START_ELEMENT){
                    System.out.println("ELEM : "+xmlsr.getLocalName());
                    if(xmlsr.getLocalName().equals("selector")){
                        System.out.println("SELECTOR");

                        String selectorName = xmlsr.getAttributeValue(null, "name");
                        Map<String, String> parameters = getParameters(xmlsr);

                        if(Selectors.isSelector(selectorName)) {
                            System.out.println("WE HAVE A NAME" + selectorName);
                            FactorySelector factory = Selectors.getFactory(selectorName);
                            selector = factory.createSelector(parameters);
                        }
                        break;
                    }
                }
            }
        } catch (XMLStreamException e) {
            throw new RuntimeException("Error with the stream!\n"+e.getMessage());
        } catch (FileNotFoundException e) {
            throw new RuntimeException("Can't find the \"poir.xml\" file\n"+e.getMessage());
        }

        if(selector==null){
            System.out.println("WE HAVENT ANY SELECTOR");
            selector = new SelectorPercentOfClasses();
        }
        System.out.println("END==============================================");

    }

    private Map<String, String> getParameters(XMLStreamReader xmlsr) throws XMLStreamException{
        Map<String,String> parameters = new HashMap<>();
        int eventType;
        while(xmlsr.hasNext()){
            eventType = xmlsr.next();
            if(eventType== XMLEvent.END_ELEMENT && xmlsr.getLocalName().equals("selector")){
                System.out.println("ON QUITTE SELECTOR");
                break;
            }
            if(eventType == XMLEvent.START_ELEMENT){
                System.out.println(xmlsr.getLocalName()+"\n"+xmlsr.getText());
                parameters.put(xmlsr.getLocalName(),xmlsr.getText());
            }
        }
        return parameters;
    }

    public static SelectorController getInstance(){
        if (_instance == null){
            _instance = new SelectorController();
        }
        return _instance;
    }

    public ISelector getSelector(){
        return selector;
    }

}
