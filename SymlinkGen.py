from elevate import elevate
import time
import os

# Elevates the program's privaleges to make it so that the mklink command actually works.
elevate()

# It didn't want to push so i have to edit so it actually pushes

# Basic base for aksing for the source file path to allow to have shorter code, while-
# allowing for normal and hardlink symlinks to be created in their own block of code.
def slinkfile():
    global filedest, filetarget
    print("Enter the Source File Path:")
    filetarget = input("[SourcePath]> ")
    print("Enter the Destination File Path:")
    filedest = input("[DestinationPath]> ")

def slinkdir():
    global dirtarget, dirdest
    print("Enter the Source Directory Path:")
    dirtarget = input("[SourcePath]> ")
    print("Enter the Destination Directory Path:")
    dirdest = input("[DestinationPath]> ")

processfinished = False

print("SymlinkGen v1.0.0")
print("A. Windows")
print("B. Unix-based (Not supported YET!!!dsfojgthn)")
ossel = input("[A/B]> ")
if ossel == "A" or "a":
    # RunLoop to allow for the code to be run again if an error occurs or if the user want to create multiple symlinks.
    while processfinished == False:
        print("Select symlink type:")
        print("1. File (Normal)")
        print("2. File (Hardlink)")
        print("3. Directory (Normal)")
        print("4. Directory (Junction)")
        print("5. Cancel")
        choice = input("[#]> ")
        if choice == "1":
            slinkfile()
            os.system(f'mklink "{filedest}" "{filetarget}"')
            print("Symlink (File) created! Would you like to run again?")
            rerun = input("[Y/N]> ")
            if rerun == "N":
                processfinished = True
        if choice == "2":
            print("Do you know what a Hardlink is?")
            hlknow = input("[Y/N]> ")
            if hlknow == "N":
                print("A hardlink is a mutation of a normal symbolic link.")
                print("If you move any of the files they will still be linked together.")
                print("A hardlink is INVISIBLE; please take note of which file is the target, and which is the destination,")
                print("also if its hardlinked in the first place. Each file must also be on the same drive volume (essentially")
                print("the same drive letter).")
                print("Do you still want to make a hardlink?")
                safetyhl = input("[Y/N]> ")
                if safetyhl == "Y":
                    slinkfile()
                    os.system(f'mklink /H "{filedest}" "{filetarget}"')
                    print("Symlink (File (Hardlink)) created! Would you like to run again?")
                    rerun = input("[Y/N]> ")
                    if rerun == "N":
                        processfinished = True
                elif safetyhl == "N":
                    print("Would you like to run again?")
                    rerun = input("[Y/N]> ")
                    if rerun == "N":
                        processfinished = True
        if choice == "3":
            slinkdir()
            os.system(f'mklink /D "{dirdest}" "{dirtarget}"')
            print("Symlink created! Would you like to run again?")
            rerun = input("[Y/N]> ")
            if rerun == "N":
                processfinished = True
        if choice == "4":
            print("A junction is not recommended as it is legacy.")
            print("If you have a specific reason to use a junction, please use it.")
            print("Would you use the junction method of directory symlink?")
            legacydirsym = input("[Y/N]> ")
            if legacydirsym == "Y":
                slinkdir()
                os.system(f'mklink /J "{dirdest}" "{dirtarget}"')
                print("Symlink created! Would you like to run again?")
                rerun = input("[Y/N]> ")
                if rerun == "N":
                    processfinished = True
        if choice == "5":
            processfinished = True
            time.sleep(5)
        else:
            print("Invalid input! Please try again.")
            print("Please choose another option.")
            time.sleep(1)
elif ossel == "B" or "b":
    print("ts pmo icl 💔💔💔")
    print("jokes aside, i genuinely dont feel like doing this rn so check the next update")
    time.sleep(5)
elif ossel == "C" or "c":
    print("why did you genuinely think that this would work")
    time.sleep(1)
    print("no like seriously")
    time.sleep(1)
    print("why")
    time.sleep(1)
    print("you have to restart to do something again; i didn't put this in the runloop")
    time.sleep(5)
else:
    print("Invalid input! Please try again.")
    print("Run the program again.")
print("Thanks for using SymlinkGen! See you next time!")
time.sleep(5)