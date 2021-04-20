
def cmdLineOutput(statement, change, reason):

    print(str(statement))
    print("Resolution: " + change)
    print(reason)

    confirmation = input("Accept Changes Y/N? ").upper()

    if confirmation == "Y":
        return True
    else:
        return False
