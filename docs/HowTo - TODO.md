# STATAMUTATION #

#################
#    TUTORIAL   #
#################

I. CONFIGURATION & EXECUTION

	1. Preparing Spoon

cd ./Mr.Stataspoon
mvn install
	
	
	2. Executing tests
	
cd ./Mr.Stataven
mvn package
	
	
	3. Preparing report
	
cd ./Mr.Statapython
python setup.py install


	4. Generate reports
	
cd ./Mr.Statapython
python -m statapython -p ../Mr.Stataven


NB : python command can be used with "py" alias according to your python configuration