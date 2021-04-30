import re

def identifySubQueries(query):
    openingParenthesis = list()
    subQueries = {}

    subre = re.compile("(?i)\(\s*(select)")

    for index in range(0, len(query)):
        character = query[index]

        if character == "(":
            openingParenthesis.append(index)

        elif character == ")":
            if not openingParenthesis:
                print("Opening Parenthesis Missing")

            else:
                startIndex = openingParenthesis.pop()
                if subre.match(query[startIndex:index + 1]) is not None:
                    subQueries[startIndex] = index + 1

    return subQueries

def findAll(searchString, query):
    index = query.find(searchString)
    while index != -1:
        yield index
        index = query.find(searchString, index + 1)
