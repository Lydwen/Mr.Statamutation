[ DevOps - Group 01 ]

	DALL'AGNOL Tom
	BUISSON Kévin
	ROLLIN Antoine

	--------------
	 STATAMUTATOR
------------------------
	SPECIFICATIONS
------------------------

#I. Project Description

This project aims at building a software architecture able to automatize testing operations on mutated program, 
using tools such as Maven, Spoon and jUnit. This is the Mutation Testing. 
A mutated program is a program on which has been applied a mutation. 
A mutation consists in modifying, removing or adding a part of a program.


#II. Tools

Several tools will be used for this project in order to facilitate and automatize the process.

##1. Mutations
###a. Spoon 
		
Spoon leverages to provide super fast sandboxes for developers and testers to spin up test environments.
It will be used because it rapidly rollbacks changes and execute tests and accelerates test cycles by eliminating 
the need to install application dependencies and modify configuration.

###b. Mutators

A set of mutators will be created, which define the way source code will be changed. 
Three kind of mutators will be defined : a mutator for the add of code, a mutator for code replacement,
and a mutator for removing code. 		

###c. Selectors

A set of selectors will be implemented, which define the part of code that will be modified 
or where a new code will be added. Also, several types of selector will be defined, according
to the number of files that has to be mutated, and to the number of mutations that has to be done. 

##2. Building with Maven

Maven is a build automation tool used primarily for Java projects. It describes how software is built 
and describes its dependencies. Maven comes with pre-defined targets for performing certain well-defined 
tasks such as compilation of code and its packaging.
It will be used for the automation of the mutated programs compilations.

##3. Testing with JUnit

JUnit is a unit testing framework for the Java programming language. 
It will be used for testing the mutated code by determining weither or not the program has failed.
Tests consists in a set of assertions about code functionalities. 

##4. HTML Report
	
Results of the testing part will be defined in XML files. Thoses files will be used to generate statistics, 
and formatted as an HTML report.
	
	
#III. Build Chain

We will have a bash script which will generate mutants, compile them, test them and then it will launch the generation of the html report.
The process will consist in a set of operations.


![Image of the build chain](https://github.com/Lydwen/Mr.Statamutation/blob/master/data/images/cycle%20build.png "The build chain")

####1. SOURCE CODE -> MUTATED CODE

- Entry : 
  * Source code
  * A set of selectors
  * A set of mutation

- Exit : a set of Mutants

- With Spoon, we will generate a mutant for each pair (mutation,selector) that we have.

####2. MUTATED CODE -> COMPILATION

- Entry : a mutant
- Exit : Bytecode

- With maven we will launch the compilation of the mutant.

####3. COMPILATION -> TESTING -> REPORT
	
- Entry : the compiled program we want to test
- Exit : the XML report of JUnit

- Thanks to JUnit we will test the mutant and then have an xml report. Thanks to maven, we will launch all of them automatically. 

####5. REPORTS -> HTML REPORT
	
- Entry : a set of reports
- Exit : a report in HTML
 
- A java program will take all the reports in entry and use them to generate a HTML page with charts to have a better view of how great is our source code.

#IV. Mutators

A mutation is a source code modification. We will use at least these mutations :
- replace "+" by "-" and conversely
- replace "<" by ">" and conversely (same for ">=" and "<=")
- replace "<" by "<=" and conversely (same for ">")
- replace "!=" by "==" and conversely
- replace "<" by "==" and conversely (same for ">", "<=", ">=")
- add "!" in front of conditions (or remove it)
- replace "++" by "--" and conversely (same for "+=", "-=")
- replace "+1" by "+2" (only numerical entities - same for "-") 
- replace "/" by "*" and conversely
- replace "&" by "&&" (same for "|")
- replace "&" by "|" (same for "&&")
- change conditions order ("X && Y" becomes "Y && X")
- if "extends", delete override methods
- replace "public" by "private" and conversely
- add or remove "final" in front of variable declarations
- replace return values by "NULL"
- replace object declaration by "NULL"
- remove/replace function called 

Mutator model :
- type (add, replace, remove)
- an entity to replace (or set of entities)
- a replacing entity  (or set of entities - or nothing)


#V. Selectors

A selector is a specifier describing where to apply mutation (which file, etc.).
We will have three kind of mutations : ONE, ALL, PERCENTAGE OF, applied on **files** (equivalent to classes in Java) and **occurrences**.
Of course, the percentage is configurable, so there are a lot of possibilites for selections.
By combination, every availables mutations are : 
- apply mutation to **ALL** FILES           & **ALL** OCCURRENCES 
- apply mutation to **ALL** FILES           & **ONE** OCCURRENCE
- apply mutation to **ALL** FILES           & **PERCENTAGE OF** OCCURRENCES
- apply mutation to **ONE** FILE            & **ALL** OCCURRENCES 
- apply mutation to **ONE** FILE            & **ONE** OCCURRENCE
- apply mutation to **ONE** FILE            & **PERCENTAGE OF** OCCURRENCES
- apply mutation to **PERCENTAGE OF** FILES & **ALL** OCCURRENCES 
- apply mutation to **PERCENTAGE OF** FILES & **ONE** OCCURRENCE
- apply mutation to **PERCENTAGE OF** FILES & **PERCENTAGE OF** OCCURRENCES

Selector model :
- source file(s) to apply mutation on
- type (unit or percent)
- number of "entity to replace" that will be replaced in the selected files  


#VI. References

- Mutation Testing : https://en.wikipedia.org/wiki/Mutation_testing
- Spoon : https://spoon.net/docs
- JUnit : https://en.wikipedia.org/wiki/JUnit
- Maven : https://en.wikipedia.org/wiki/Apache_Maven
