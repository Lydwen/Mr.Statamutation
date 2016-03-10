# Mr.Statamutation :: Rapport#

## Feedback ##
	
Ce projet a permis de comprendre la modification de code avec 
Spoon et de nous familiariser davantage avec Maven. 
Il a également permis de raviver nos connaissances du language
Python.

Nous pensons avoir bien travaillé puisque nous sommes parvenus
à réaliser une application fonctionnelle qui répond aux
besoins énoncé par le probleme.

Plusieurs pistes d'améliorations sont possibles. Avec plus de temps (ne jamais négliger le prochain sprint !), 
les axes suivants auraient pu, par exemple, être améliorés/implémentés :
- plus de processeurs
- plus de sélecteurs
- améliorer le rapport (graphiques présentés, détails par mutations, etc.)
- paralélliser la chaine de build (plusieurs mutations en même temps)


## Analyse du programme ##

### Points positifs ###

> Portabilité

Le projet ne se base que sur des technologies qui sont multi-plateformes, à savoir :
	- les langages Java et Python
	- le framework Maven

Par conséquent, notre projet est portable sur plusieurs toutes les plateformes sur lesquelles ces technologies le sont.

	
> Facile à utiliser

L'ensemble de l'éxécution de la chaine de build s'effectue par l'appel d'une simple commande.

De plus, les configurations sont effectués grâce à des fichiers XML (langage human-readable), et par conséquent simples de compréhension.


> Installation rapide 

...

> Rapport HTML
	
Le rapport inclut les résultats des tests de toutes les mutations.
Il permet l'identification des tests qui ont échoué pour toute les
mutations.

Le rapport est élégant et dispose de graphiques qui facilitent la
compréhension des résultats


### Points négatifs ###

> Rapport HTML

Le rapport affiche la liste des mutations qui ont un pourcentage de 
tests réussi supérieur ou égal au pourcentage de tests de la version 
non-mutée. Néanmoins, il ne permet pas de comprendre les raisons pour
lesquelles une mutation a obtenu de meilleurs résultat que l'original.

De plus, le fichier HTML n'est pas facile à modifier, en raison de
l'utilisation de Jinja qui permet d'injecter du code.


> Temps d'exécution
	
Le programme peut devenir très lent pour un nombre important de mutations
et de tests. Le parallèlisme aurait pu être utilisé en lançant chaque
test dans un thread, utilisant ainsi les capacités du processeur 
multi-coeurs.