# Mr.Statamutation :: How To... #

## 1. Installation ##

Voir le fichier **Build.md**.

## 2. Configuration ##

### Configuration du projet à muter ###

Dans un premier temps, il est nécessaire de configurer le projet à muter. \s\s
Pour ce faire, il faut rajouter le code suivant dans le **pom.xml** :
~~~xml
			<plugin>
				<groupId>fr.inria.gforge.spoon</groupId>
				<artifactId>spoon-maven-plugin</artifactId>
				<version>2.2</version>
				<executions>
					<execution>
						<phase>generate-sources</phase>
						<goals>
							<goal>generate</goal>
						</goals>
					</execution>
				</executions>
				<!-- To be sure that you use the latest version of Spoon, specify it as dependency. -->
				<dependencies>
					<dependency>
						<groupId>fr.inria.gforge.spoon</groupId>
						<artifactId>spoon-core</artifactId>
						<version>5.0.2</version>
					</dependency>
					<dependency>
						<groupId>--- votre groupe ---</groupId>
						<artifactId>--- votre artefact ---</artifactId>
						<version>--- votre version ---</version>
					</dependency>
					<!-- Il est évidemment possible d'ajouter autant de dépendances que vous souhaitez. -->
				</dependencies>
			</plugin>
~~~

### Configuration des mutations à appliquer ###

Dans un second temps, il est nécessaire de configurer les mutations et sélécteurs associés, à appliquer à votre projet. \s\s
Pour ce faire, il faut créer un fichier **statamutations.xml** à la racine de votre projet. Le fichier doit être de la forme suivante : 
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<statam>
	<mutations>
		<mutation>
			<name>Mutation plus to minus</name>
			<processors>
				<processor>fr.polytech.devops.g1.stataspoon.processors.operators.binary.InfEqToSupEqProcessor</processor>
				<processor>fr.polytech.devops.g1.stataspoon.processors.operators.binary.EqToIneqProcessor</processor>
			</processors>
			<selector name="PercentClass">
				<parameters>
					<percent>30</percent>
				</parameters>
			</selector>
		</mutation>
		<!-- Il est possible de configurer autant de mutations que voulu. -->
	</mutations>
</statam>
~~~

## 3. Exécution ##

Du moment que vous avez suivi les étapes précédentes, la chaine de build s'exécute avec une simple commande, dans le dossier du projet :
~~~shell
	python -m statapython
~~~

Le programme va alors appliquer les tests sur le projet original, puis effectuer chacune des mutations configurées et y appliquer les tests. \s\s
Un rapport est ensuite généré. L'ensemble des résultats est alors disponible dans le dossier **./target/statam-report/**.
	
Un certain nombre de paramètres est disponible, à savoir pour les plus importants :
- **--project** (**-p**) : Spécifie le dossier du projet à build.
- **--mutations-config** (**-m**) : Spécifie le fichier de configuration des mutations à appliquer.

Pour avoir un détail complet des options : **--help** (**-h**)