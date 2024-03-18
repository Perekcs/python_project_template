from app.io.input import *
from app.io.output import *


def main():
    consoleOutput(consoleInput())
    fileOutput(consoleInput())

    consoleOutput(fileInput())
    fileOutput(fileInput())

    consoleOutput(pandasInput())
    fileOutput(pandasInput())



if __name__ == "__main__":
    main()
