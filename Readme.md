# Salt

Salt is a custom Python web framework built from scratch.

Case Study OutCome: Allows less experienced developer understand how a modern python framework(`Flask, Django, FastAPI`) works under the hood.

## Directory Structure
```
Salt/
├── Makefile
├── core/
│   ├── __init__.py
│   ├── app.py
│   └── tests/
│       ├── __init__.py
│       └── test.py
├── .gitignore
└── changelog.md
```

## Evolution

Conventional Commits is a specification for adding human and machine-readable meaning to commit messages. It provides a set of rules for creating an explicit commit history, which makes it easier to write automated tools on top of the commit history.

Each commit message should start with a type, followed by a colon and a space, and then a brief description of the changes made in the commit. The type can be one of the following:

- `feat`: a new feature
- `fix`: a bug fix
- `docs`: changes to documentation
- `style`: formatting, missing semi colons, etc; no code change
- `refactor`: refactoring production code
- `test`: adding tests, refactoring test; no production code change
- `chore`: updating build tasks, package manager configs, etc; no production code change

By following this convention, you can easily navigate the commit history and understand the changes made to the project over time.


## File Intents:
The "File Intents" section in the README file is meant to provide a brief description of the purpose of each file and directory in the project's directory structure. This information can be useful for developers who are new to the project and need to quickly understand what each file and directory is for. It can also serve as a reference for developers who are already familiar with the project but need a quick reminder of what a particular file or directory is used for:
- `Makefile`: a file that contains instructions for the `make` utility
- `core/`: a directory that contains the core application code
- `core/__init__.py`: an empty file that marks the `core` directory as a Python package
- `core/app.py`: a file that contains the main application code
- `core/tests/`: a directory that contains the unit tests for the application
- `core/tests/__init__.py`: an empty file that marks the `tests` directory as a Python package
- `core/tests/test.py`: a file that contains the unit tests for the application
- `.gitignore`: a file that specifies files and directories that should be ignored by Git
- `changelog.md`: a file that contains a log of changes to the project
 

## Prerequisties

To run this project it's essential to create a sepperate envs where to store the all the project's dependencies.

- Install  `pip install virtualenvwrapper`
- Follow this instructions: source[virtualenvwraper]('https://virtualenvwrapper.readthedocs.io/en/latest/') to create a virtual env wrappper named `salt`
```
$    export WORKON_HOME=~/Envs
$    mkdir -p $WORKON_HOME
$    which virtualenvwrapper.sh
$    source {printed/virual/path}/virtualenvwrapper.sh
```

- Activate `salt` and you will see this(Fig 1.1)




![Figure 1.1: salt-env](salt-env.png "Figure 1.1: Salt environment")

- if you ever get out of the enviroment feel free to activate it by `workon salt`



Now that you have setup the salt env you will have access to the Make file commands
which will make it easier to manage the project

_if make commands to do work ensure that they can be executed `chmod +x Makefile`_


# Start
Unload the projects dependies in the project
`make install`

Run the project Fig:1.2
`make app`


![Fig:1.2: salt-server](salt-server.png "Fig:1.2: salt-server")


To give better context of this project I follow [Convetional Commits]('https://www.conventionalcommits.org/en/v1.0.0/'] to give context to the evolution of changes throught out the project.

