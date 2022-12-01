#!/bin/python3


#1- Create directory with the name of project
#2- Create main.py file inside project directory
#3- Create python virtual environment
#4- Create requirements.txt file
#5- Initialize git repository
#6- Write main function into main.py file

import sys                   # Allows us to add more arguments when running the app in terminal
import subprocess            # Allows us to run mkdir,touch, cd, ls, cat
# print(sys.argv)
# print(sys.argv[1])

argv = sys.argv


def main():
    debug = False
    vscode = False


    if len(argv) < 2:
        print("Please pass project name")
        sys.exit()

    if argv[1] == "--help" or argv[1] == "-h":
        print("""
Usage: main.py [OPTION]... [PROJECT]...
Generate python project at /jurgenmane/dev/

--help     display this help and exit
""")
        sys.exit()

    if "-d" in argv or "--debug" in argv:
        debug = True

    
    if "-v" in argv or "--vscode" in argv:
        vscode = True 

    
    #argv = ["./main.py", "-v", "--debug", "test"]

    name = None
    for arg in argv:
        if arg[0] != "-" and arg != "./main.py":
          name = arg  

    if name != None:
        project_name = "/home/jurgenmane/dev/" + name # name of project



    subprocess.run(["mkdir", project_name], capture_output=True)

    if debug:
        print("Creating project at " + project_name)

        
    main_file = project_name + "/main.py"
    subprocess.run(["touch", main_file], capture_output=True)
    if debug:
        print("Creating main.py file at " + main_file )


    virtual_env = project_name + "/venv"
    subprocess.run(["python3", "-m", "venv", virtual_env], capture_output=True)
    if debug:
        print("Creating virtual environment at "+ virtual_env)


    requirement_file = project_name + "/requirement.txt"
    subprocess.run(["touch", requirement_file], capture_output=True)
    if debug:
        print("Creating requirement file at " + requirement_file)

    subprocess.run(["git", "init", project_name], capture_output=True)
    if debug:
        print("Creating git repository at" + project_name)

    file = open(main_file, "w")
    main_function = "def main():\n\n\n\n\n\nmain()"
    file.write(main_function)
    if debug:
        print("Writing main function at " + main_file + " ...")

    #subprocess.run(["echo", main_function, ">>", main_file])

    if vscode:
        subprocess.run(["code", project_name])


main()        
