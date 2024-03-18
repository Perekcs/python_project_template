def consoleInput():
    """
    Function to input text from the console.
    """
    return input("How old are you?: ")

def fileInput():
    """
    Function to read from a file.
    """
    filePath = "data/data.txt"
    try:
        with open(filePath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def pandasInput():
    """
    Function to read from a file using the pandas.
    """
    import pandas as pd
    filePath = "data/csv_data.csv"
    try:
        data = pd.read_csv(filePath)
        return data.to_string()
    except FileNotFoundError:
        return "File not found."
