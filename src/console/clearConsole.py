import os
import platform


# Clear console output
def clearConsole():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    return None


# OSX and Linux full clear:
# os.system("printf '\33c\e[3J'")