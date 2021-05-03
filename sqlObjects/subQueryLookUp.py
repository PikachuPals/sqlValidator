import re

def identifySubQueries(query):
    openingParenthesis = list()
    subQueries = {}

    # Identifies (select of any case.
    subre = re.compile("(?i)\(\s*(select)")

    # Iterate through and find matching parenthesis.
    for index in range(0, len(query)):
        character = query[index]

        if character == "(":
            openingParenthesis.append(index)

        elif character == ")":
            if not openingParenthesis:
                print("Opening Parenthesis Missing")

            else:
                startIndex = openingParenthesis.pop()

                # If regex matches, it is a subquery.
                if subre.match(query[startIndex:index + 1]) is not None:
                    subQueries[startIndex] = index + 1

    return subQueries
