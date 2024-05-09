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
    userdirectory = str(input("Please enter complete directory path, including the final filename and extension:\n"))

    #filename = str(input("Please enter filename complete with any file extension:\n")

    """This line allows the filename alone to be entered as it's own argument to the DV command."""
    #subprocess.check_output(['/usr/local/bin/dolby_vision_professional_tools/metafier', '-validate', userdirectory, filename])

    subprocess.check_output(['/usr/local/bin/dolby_vision_professional_tools/metafier', '-validate', userdirectory])
    input("Return to finish")
    input("Hit enter to close console")#
    

if __name__ == "__main__":
    menuOpt = Menu()
    
