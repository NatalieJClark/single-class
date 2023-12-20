# TDD and Design of Single Class Programs

## Introduction
- This is my repo for Makers Module 2 - Golden Square: Test Driving and Designing Single Class Programs
- It contains practise code for learning how to use TDD and design recipes to make single class programs
  
## Objectives
I used this project to learn how to:
- [x] Test-drive a single-class program
- [x] Design a single-class program

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...
```
To test the practise code: 
```shell
# Install the dependencies (pytest)
; pipenv install # NB: you may need to change interpreters to import pytest

# Optionally ...
# Activate the project's virtualenv
; pipenv shell

# cd into the relevant directory:
; cd 1_test_drive_single_class # Practise code for TDD of single class programs
; cd 2_design_single_class # Practise code for designing single class programs

# If using the pipenv shell:
# This runs all of the tests in the current directory
; pytest
# And this exits the pipenv shell
; exit # or Ctrl-D

# Otherwise, this runs all of the tests in the current directory
; pipenv run pytest
```
