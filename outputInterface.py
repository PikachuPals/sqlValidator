
def cmdLineOutput(statement, change, reason):

    print(str(statement))
    print("Resolution: " + change)
    print(reason)

    confirmation = input("Accept Changes Y/N?")

    if confirmation:
        return True
    else:
        return False
