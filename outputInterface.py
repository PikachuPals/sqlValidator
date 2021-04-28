cmdline = True

def cmdLineOutput(statement, change, reason):

    seperatorText = "-" * 25
    print("\n" + seperatorText)
    print("/\n| Query:")
    print("|         " + str(statement))
    print("\n|  Resolution:")
    print("|         " + change)
    print("\n|  Explanation:\n|")
    print("\         " + reason)

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
