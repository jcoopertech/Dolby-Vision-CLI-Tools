import subprocess
# Python Interpreter for Dolby Vision Tools
# Written by coding@jcooper.tech - contact here for any info.
# Tested remotely by others.

def Menu():
    print("""
Dolby Vision Tools Lines
Written by coding@jcooper.tech

This software provides no checks for filenames being correct, and assumes that DV Tools will do this.


Which option would you like:

Option 1. Validate XML
Option 2. Fix Dissolves in XML
Option 3. Upgrade / Downgrade XML
Option 4. Analyse a ProRes for HD10 Meta""")
    try:
        return int(input("Please choose [1/2/3/4] as a number only.: "))
    except:
        print("\n\n\n!!! >> You entered an invalid response")
        raise

def option1(userdirectory):
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '—validate', userdirectory], stdout=subprocess.PIPE)
    result.stdout

def option2(userdirectory):
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '--fix-dissolves', userdirectory], stdout=subprocess.PIPE)
    result.stdout

def option3():
    old = str(input("Input file path of XML to upgrade to latest DV Meta Version: "))
    new = str(input("Input file name of updated XML (Don’t include .XML at the end): "))+".xml"
    print (new)
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '-o', new, '--save-version', 'latest', old], stdout=subprocess.PIPE)
    result.stdout

def option4():
    framerate = str(input("Please enter Frame Rate of ProRes file: "))
    startframe = str(input("Please enter starting frame number: "))
    endframe = str(input("Please enter end frame number: "))
    aspectratio = str(input("Please enter Aspect Ratio (e.g: 1.77778): "))
    in_file = str(input("Please enter ProRes File location: "))
    xml_loc = str(input("Please enter output xml file location >> Do not include extension, but include filename: "))
    fr_concat = startframe+"-"+endframe
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/cm_analyze',\
                             '-m', '21', \
                             '-r', framerate, \
                             '-f', fr_concat, \
                             '--source-format', "u10 p422 lsb32rev le 422 ycbcr_bt2020 computer pq bt2020", \
                             '--aspect-ratios', aspectratio, aspectratio, \
                             '--bda', in_file, xml_loc+".xml"], stdout=subprocess.PIPE)
    result.stdout


if __name__ == "__main__":
    menuOpt = Menu()
    if menuOpt == 1 or menuOpt == 2:
        fil = str(input("Please enter complete directory path, including the final filename and extension: "))

    if menuOpt == 1:
        option1(fil)
    elif menuOpt == 2:
        option2(fil)
    elif menuOpt == 3:
        option3()
    elif menuOpt == 4:
        option4()
    input("Return to finish")
    input("Hit enter to close console")#
