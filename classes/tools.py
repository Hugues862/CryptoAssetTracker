import json
from os import system, name


def writeToFile(data, name):
    with open('./json/'+name, "w") as file:
        json.dump(data, file)


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
