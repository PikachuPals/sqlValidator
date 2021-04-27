cmdline = True

def cmdLineOutput(statement, change, reason):

    print("\n\n\nQuery:")
    print("         " + str(statement))
    print("\nResolution:")
    print("         " + change)
    print("\nExplanation:\n")
    print("         " + reason)

    confirmation = input("\nAccept Changes Y/N? ").upper()

    if confirmation == "Y":
        return True
    else:
        return False

def output(statement, change, reason):
    input = False;
    if cmdline:
        input = cmdLineOutput(statement, change, reason)

    return input
