import pyperclip

from config import cmdLine, replIt
import sqlparse

def cmdLineOutput(statement, change, reason):

    seperatorText = "-" * 25
    print("\n" + seperatorText + "\n")
    print("/\n| Query:")
    print("|        " + str(statement))
    print("\n|  Resolution:")
    print("|        " + change)
    print("\n|  Explanation:\n|")
    print("\        " + reason)

    confirmation = input("\nAccept Changes Y/N? ").upper()

    if confirmation == "Y" or confirmation == "YES":
        return True
    else:
        return False

def output(statement, change, reason):
    input = False;
    if cmdLine:
        input = cmdLineOutput(statement, change, reason)

    return input

def finalQueryOutput(mainQuery, queryStatements):

    finalQuery = sqlparse.format(mainQuery.query.format(*queryStatements.values()),
     keyword_case = "upper", reindent_aligned = True, indent_width = 4)

    seperatorText = "-" * 25

    print("\n" + seperatorText + "\n")
    print("\nFinal Resolved Query:\n")
    print(finalQuery)
    print("\n")

    if not replIt:
        confirmation = input("Copy to Clipboard Y/N? ").upper()

        if confirmation == "Y" or confirmation == "YES":
            pyperclip.copy(finalQuery)

def outputFinalQuery(mainQuery, queryStatements):
    if cmdLine:
        finalQueryOutput(mainQuery, queryStatements)
