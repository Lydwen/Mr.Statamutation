#!/usr/bin/python
import os
import shutil
import stat


def my_copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)
    lst = os.listdir(src)
    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]
    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except:
                pass  # lchmod not available
        elif os.path.isdir(s):
            my_copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def copy_files(src, dest, nb_mutant=0):
    for mutant_number in range(0, nb_mutant):
        print("Mutant num", mutant_number, "\n")
        dest_folder = dest + "/mutant_" + str(mutant_number)
        print("Place them into ", dest_folder)

        my_copytree(src, dest_folder)
    return

# === Main ===
if __name__ == "__main__":
	# Go to script directory
	os.chdir(os.path.dirname(__file__))
	
	# Original tests
	print('\n\n===================== Programme original =====================\n\n')
	os.system('mvn clean -Dstataprocessor="fr.polytech.devops.g1.stataspoon.NeutralProcessor" package')
	my_copytree('./target/surefire-reports', './test-report/original')

	# First mutation tests
	print('\n\n===================== Programme avec mutations =====================\n\n')
	os.system('mvn clean -Dstataprocessor="fr.polytech.devops.g1.stataspoon.PlusToMinusProcessor" package')
	copy_files('./target/surefire-reports', './test-report', 1)
	
	# Run reporting
	print('\n\n===================== Generation du report =====================\n\n')
	os.chdir('../Mr.Statapython')
	os.system('python -m statapython.report "../Mr.Stataven/test-report" -o "../Mr.Stataven/test-report/report.html"')
	
	print("#swag j'ai fini\n")

