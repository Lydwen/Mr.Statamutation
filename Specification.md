[ DevOps - Group 01 ]

------------------------
	SPECIFICATIONS
------------------------

Build Chain

blablabla


Tools

- .java
- mutators
- locators
- jUnit
- Maven
- result.xml
- ...


Mutations

A mutation is a source code modification.

- replace "+" by "-" and backward
- replace "<" by ">" and backward (same for ">=" and "<=")
- replace "<" by "<=" and backward (same for ">")
- replace "!=" by "==" and backward
- replace "<" by "==" and backward (same for ">", "<=", ">=")
- add "!" in front of conditions (or remove it)
- replace "++" by "--" and backward (same for "+=", "-=")
- replace "+1" by "+2" (only numerical entities - same for "-") 
- replace "/" by "*" and backward
- replace "&" by "&&" (same for "|")
- replace "&" by "|" (same for "&&")
- change boolean values
- change conditions order ("X && Y" becomes "Y && X")
- if "extends", delete override methods
- replace "public" by "private" and backward
- add or remove "final"


Mutator model :
- type (add, replace, remove)
- an entity to replace (or set of entities)
- a replacing entity  (or set of entities - or nothing)


Locators

A locator is a specifier describing where to apply mutation (which file, etc.)

- apply mutation to ALL FILES & ALL OCCURRENCES 
- apply mutation to ONE FILE & ALL OCCURRENCES
- apply mutation to ONE FILE & ONE OCCURRENCE
- apply mutation to ALL FILES & A CERTAIN PERCENTAGE OF OCCURRENCES (ex: apply mutation to 60% of the file)
- apply mutation to ONE FILE & A CERTAIN PERCENTAGE OF OCCURRENCES
