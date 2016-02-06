[ DevOps - Group 01 ]

	DALL'AGNOL Tom
	BUISSON Kévin
	ROLLIN Antoine

	--------------
	 STATAMUTATOR
------------------------
	SPECIFICATIONS
------------------------

I. Project Description

This project aims at building an architecture able to automatize testing operations on mutated program, using tools such as Maven, Spoon and jUnit.
A mutated program is a program on which has been applied a mutation. A mutation consists in modifying, removing or adding a part of a program.


II. Tools

Several tools will be used for this project in order to facilitate and automatize the process.

	1. Mutations
	
		a. Spoon 
		
		b. Mutators
		
		c. Selectors
		
		
	2. Testing with jUnit


	3. Building with Maven

	
	4. Reports as XML files


	

III. Assembly Line

	1. SOURCE CODE -> MUTATED CODE

- Source code
- Mutators
- Selectors
- Spoon
	
	
	2. MUTATED CODE -> COMPILATION

- Javac
- Bytecode
	
	
	3. COMPILATION -> TESTING
	
- JUnit
	
	
	4. TESTING -> REPORT

- XML files


	5. AUTOMATIZATION
	
- Maven


IV. Mutations

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
- remove/replace function called 

Mutator model :
- type (add, replace, remove)
- an entity to replace (or set of entities)
- a replacing entity  (or set of entities - or nothing)


V. Selectors

A selector is a specifier describing where to apply mutation (which file, etc.).
We will at least use these ways for mutation applications :
- apply mutation to ALL FILES & ALL OCCURRENCES 
- apply mutation to ONE FILE & ALL OCCURRENCES
- apply mutation to ONE FILE & ONE OCCURRENCE
- apply mutation to ALL FILES & A CERTAIN PERCENTAGE OF OCCURRENCES (ex: apply mutation to 60% of the file)
- apply mutation to ONE FILE & A CERTAIN PERCENTAGE OF OCCURRENCES

Selector model :
- source file(s) to apply mutation on
- type (unit or percent)
- number of "entity to replace" that will be replaced in the selected files  