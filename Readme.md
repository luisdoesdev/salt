 

# 🚧 WIP ver 0 👷🏿‍♂️ 🚧

## Salt🧂

## The Case Study to Demystify Modern Python Web Frameworks
Deepen your understanding of Python web frameworks like Flask, Django, and FastAPI with this comprehensive case study. Explore, learn, and master the art of web development.


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
 

## Prerequisites
To run this project, it's essential to use Docker, which allows you to package the application and its dependencies into a container that can run on any computing environment.

Install Docker following the instructions on the official Docker documentation.
Building the Docker Image
Build the Docker image for the Salt application. Navigate to the project directory and run:

bash
Copy code
$ docker build -t salt-app .
This command builds the Docker image using the Dockerfile in the current directory and tags it as salt-app.
Running the Application
To run the Salt application inside a Docker container, use the following command:

bash
Copy code
$ docker run -p 8000:8000 salt-app
This command runs the Docker container and maps port 8000 on your machine to port 8000 on the container. Now, you should be able to access the application at http://localhost:8000 in your web browser.

Stopping the Application
To stop the Docker container running the Salt application, first find the container ID with:

bash
Copy code
$ docker ps
Then, stop the container using:

bash
Copy code
$ docker stop [CONTAINER_ID]
Replace [CONTAINER_ID] with the actual ID of your running container.

Start
With Docker, managing and running the project becomes straightforward and does not require managing dependencies on your local machine.

Running the Application
As mentioned in the prerequisites section, use the following command to run the application:

bash
Copy code
$ docker run -p 8000:8000 salt-app
Running Tests
If you have tests defined and would like to run them in a Docker environment, ensure your Dockerfile or an additional Dockerfile is set up to run tests, and use the following command:

bash
Copy code
$ docker run salt-app test
Ensure that the test command is defined in your Docker setup to run your tests.






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



# Contributing to Salt

Thank you for your interest in contributing to Salt! Here are some guidelines to help you get started.

## Reporting Bugs

If you find a bug in Salt, please open an issue on our GitHub repository and include as much detail as possible, such as:

- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any error messages or stack traces

## Submitting Feature Requests

If you have an idea for a new feature in Salt, please open an issue on the GitHub repository and include as much detail as possible, such as:

- A description of the feature
- Use cases for the feature
- Any potential drawbacks or limitations of the feature

## Contributing Code

If you would like to contribute code to Salt, please follow these steps:

1. Fork the Salt repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them to your branch.
5. Push your branch to your forked repository on GitHub.
6. Open a pull request on the Salt repository.

Please make sure to include tests for any new code you add, and make sure all tests pass before submitting your pull request.

Thank you for your interest and contributions to Salt!




MIT License

Copyright (c) 2023 Luis Torruella and Adobo Digital 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.