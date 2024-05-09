import subprocess
# Python Interpreter for Dolby Vision Tools
# Written by coding@jcooper.tech - contact here for any info.
# Tested remotely by others.

def Menu():
    print("""
Dolby Vision Tools Lines
Written by coding@jcooper.tech


Which option would you like:

Option 1. Validate XML
Option 2. Fix Dissolves in XML
Option 3. Update XML to latest DV Version
Option 4. Analyse a ProRes for HD10 Meta""")
    try:
        return int(input("Please choose [1/2/3/4] as a number only."))
    except:
        print("\n\n\n!!! >> You entered an invalid response")
        raise

def option1(userdirectory):
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '—validate', userdirectory], stdout=subprocess.PIPE)
    result.stdout

def option2(userdirectory):
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '--fix-dissolves', userdirectory], stdout.subprocess.PIPE)
    result.stdout

def option3():
    old = str(input("Input file path of XML to upgrade to latest DV Meta Version: "))
    new = str(input("Input file name of updated XML (Don’t include .XML at the end): "))
    new.append(".xml")
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '-o', new, '--save-version latest', old])

def option4():
    print("pls b patientz")

def motd():
    print("""

______      _ _                       _____  _____   _____           _     
|  _  \    | | |              ____   |  ___||  _  | |_   _|         | |    
| | | |___ | | |__  _   _    / __ \  |___ \ | |_| |   | | ___   ___ | |___ 
| | | / _ \| | '_ \| | | |  / / _` |     \ \\____ |   | |/ _ \ / _ \| / __|
| |/ / (_) | | |_) | |_| | | | (_| | /\__/ /.___/ /   | | (_) | (_) | \__ \
|___/ \___/|_|_.__/ \__, |  \ \__,_| \____/ \____/    \_/\___/ \___/|_|___/
                     __/ |   \____/                                        
                    |___/                                                  """)


if __name__ == "__main__":
    motd()
    menuOpt = Menu()
    fil = str(input("Please enter complete directory path, including the final filename and extension: "))

    if menuOpt == 1:
        option1(fil)
    elif menuOpt == 2:
        option2(fil)
    elif menuOpt == 3:
        option3(fil)
    elif menuOpt == 4:
        option4(fil)
    input("Return to finish")
    input("Hit enter to close console")#
