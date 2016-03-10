# Mr.Statamutation :: Build#

## Pré-requis ##
- Java 8
- Maven 3
- Python 3, avec le package **setuptools**

### Mr.Stataspoon ###

Le projet contenant les mutations implémentées (processeurs et sélécteurs) est un projet Maven.

Cependant, celui-ci n'étant pas en ligne sur un repository officiel Maven, il est nécessaire de l'installer manuellement dans le repository local de la machine.

Pour ce faire, il faut récupérer le projet [Mr.Statapoon](./Mr.Statapoon/)

Puis, dans le dossier du projet, l'installer à l'aide de la commande :
~~~shell
	mvn install
~~~

### Mr.Statapython ###

L'exécution de la chaine de build s'effectue grâce à un module Python. Pour les mêmes raisons que **Mr.Stataspoon**
(à savoir que le projet n'est pas en ligne sur un repository officiel Python), il est nécessaire de l'installer manuellement sur la machine.

Pour ce faire, il faut récupérer le projet suivant (on commence à avoir l'habitude) : [Mr.Statapython](./Mr.Statapython/)

Puis, dans le dossier du projet, l'installer à l'aide de la commande :
~~~shell
	python setup.py install
~~~

Félicitations, vous avez déployé le projet **Mr.Statamutation** sur votre machine.
