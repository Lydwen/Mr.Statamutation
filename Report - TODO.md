# STATAMUTATION #

#################
#     RAPPORT    #
#################

I. FEEDBACK
	
Ce projet a permis de comprendre la modification de code avec 
Spoon et de nous familiariser davantage avec Maven. 
Il a également permis de raviver nos connaissances du language
Python.

- Manque de temps pour réaliser quelque chose de complet
- Beaucoup de problèmes avec Python #Antoine


II. ANALYSE DU PROGRAMME

	1. Points positifs du programme

		a. Portabilité

- Python 
- Java 

	
		b. Facile à utiliser

- Une commande et basta
	
	
		c. Installeur 

Tous les outils nécessaires (bootstrap, highcharts, etc..) au 
fonctionnement du programme  sont compressés dans des archives. 
L'installeur setup.py permet de XXX.
	
	
		d. Rapport HTML
	
Le rapport inclut les résultats des tests de toutes les mutations.
Il permet l'identification des tests qui ont échoué pour toute les
mutations.

Le rapport est élégant et dispose de graphiques qui facilitent la
compréhension des résultats


	2. Points négatifs

		a. Rapport HTML

Le rapport affiche la liste des mutations qui ont un pourcentage de 
tests réussi supérieur ou égal au pourcentage de tests de la version 
non-mutée. Néanmoins, il ne permet pas de comprendre les raisons pour
lesquelles une mutation a obtenu de meilleurs résultat que l'original.

De plus, le fichier HTML n'est pas facile à modifier, en raison de
l'utilisation de Jinja qui permet d'injecter du code.


		b. Temps d'exécution
	
Le programme peut devenir très lent pour un nombre important de mutations
et de tests. Le parallèlisme aurait pu être utilisé en lançant chaque
test dans un thread, utilisant ainsi les capacités du processeur 
multi-coeurs.