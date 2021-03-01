
def cmdLineOutput(statement, change, reason):

    print(statement)
    print(change)
    print(reason)

    confirmation = input("Accept Changes Y/N?")

    if confirmation:
        return True
    else:
        return False
