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
    if len(argv) != 2:
        print("Please pass project name")
        sys.exit()

    if argv[1] == "--help" or argv[1] == "-h":
        print("""
Usage: main.py [OPTION]... [PROJECT]...
Generate python project at /jurgenmane/dev/

--help     display this help and exit
""")
        sys.exit()

    

    project_name = "/home/jurgenmane/dev/" + argv[1]
    subprocess.run(["mkdir", project_name])

    main_file = project_name + "/main.py"
    subprocess.run(["touch", main_file])

    virtual_env = project_name + "/venv"
    subprocess.run(["python3", "-m", "venv", virtual_env])

    requiremnt_file = project_name + "/requirement.txt"
    print(requiremnt_file)
    subprocess.run(["touch", requiremnt_file])

    subprocess.run(["git", "init", project_name])

    file = open(main_file, "w")
    main_function = "def main():\n\n\n\n\n\nmain()"
    file.write(main_function)

    #subprocess.run(["echo", main_function, ">>", main_file])

    subprocess.run(["code", project_name])





main()        
