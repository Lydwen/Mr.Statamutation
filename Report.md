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
- script de déploiement du framework


## Analyse du programme ##

### Points positifs ###

> Portabilité

Le projet ne se base que sur des technologies qui sont multi-plateformes, à savoir :
<ul>
<li>les langages Java, Python et HTML</li>
<li>le framework Maven</li>
<li>le framework Spoon</li>
<li>le framework Bootstrap</li>
<li>le framework HightCharts</li>
</ul>

Par conséquent, notre projet est portable sur toutes les plateformes sur lesquelles ces technologies le sont.

	
> Utilisation facile

L'ensemble de l'éxécution de la chaine de build s'effectue par l'appel d'une simple commande.
De plus, les configurations sont effectuées grâce à des fichiers XML (langage human-readable), et par conséquent simples d'utilisation et de compréhension.


> Installation rapide 

L'installation est relativement facile et rapide. Il est juste nécéssaire de récupérer les projets, ces derniers s'installent en 2 commandes.
Aussi, le script setup.py permet l'installation de différents composants tels que les frameworks Bootstrap et Hightcharts utiles à la création du rapport HTML. 

Pour plus de détails, voir le fichier [Build.md](./Build.md).


> Rapport HTML
	
Le rapport inclut les résultats des tests de toutes les mutations.
Il permet l'identification des tests qui ont échoués pour toutes les
mutations.

Le rapport est élégant et dispose de graphiques qui facilitent la
compréhension des résultats.


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