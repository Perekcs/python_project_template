def consoleOutput(text):
    """
    Function to output text to the console.
    """
    print(text)


def fileOutput(text):
    """
    Function to write to a file.
    """
    filePath = "data\output.txt"
    with open(filePath, "w") as file:
        file.write(text)
