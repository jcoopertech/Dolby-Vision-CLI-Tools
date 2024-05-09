import subprocess
# Python Interpreter for Dolby Vision Tools
# Written by coding@jcooper.tech - contact here for any info.
# Tested remotely by others.

def Menu():
    print("""
Dolby Vision Tools Lines
Written by coding@jcooper.tech


Which option would you like:

Option 1. Validate XML""")
    """Option 2. Fix Dissolves in XML
    Option 3. Update XML to latest DV Version
    Option 4. Analyse a ProRes for HD10 Meta"""
    try:
        return int(input("Please choose [1/2/3/4] as a number only."))
    except:
        print("\n\n\n!!! >> You entered an invalid response")
        raise

def option1():
    userdirectory = str(input("Please enter complete directory path, including the final filename and extension: "))
    result = subprocess.run(['/usr/local/bin/dolby_vision_professional_tools/metafier', '-validate', userdirectory], stdout=subprocess.PIPE)
    result.stdout

    
if __name__ == "__main__":
    menuOpt = Menu()
    if menuOpt == 1:
        option1()
    input("Return to finish")
    input("Hit enter to close console")#
