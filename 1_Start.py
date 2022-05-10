
#INSTALLATION AND CODING WITH PYTHON

benefits= ["readability","libraries","community","ease of use","wide scope"]

installation= {
    1: "Install python from https://www.python.org/downloads/windows/",
    2: "For here on use windows terminal or standard console. Test installation with 'python -V' ",
}


execution={
    "1.Enter python shell":{
        1:"Initialize shell with command 'python' ",
        2:"Typing code directly into console",
        3:"Exit with command 'exit()' "
    },
    "2.PREFERRED: Running files":"From console type: python fileName.py",
}

indent="4 spaces"

print(execution)


#INSTALLATION AND CODING WITH FLASK

Step_One="Install virtual environment Globally with command:"
            pip install pipenv
        Do not have to repeat this step after globally installed
Step_Two="Navigate to project main folder and command: "
            pipenv install flask"
        Repeat for each project.

Hold_Up="IF YOU RUN INTO ANY ERRORS: Preface all pipenv commands with python-m."
        Example:  python -m pipenv <command to use>

Step_Three="In the same folder, enter the shell using command:"
    pipenv shell

Step_Four= "Exit when done using command:"
    exit