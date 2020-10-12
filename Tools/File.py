import os

def create(name:str):
    """
    Here you have to pass one perameter name
    If the folder was created it will return true
    Or if the folder already exist it will return false
    """
    try:
        os.mkdir(name)
        return True
    except FileExistsError:
        return False

def goto(location:str):
    """
    Here you have to pass one perameter location
    It will return a boolean value True or False
    """
    try:
        os.chdir(location)
        return True
    except FileNotFoundError:
        return False