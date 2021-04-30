from . import subQueryLookUp as subQuery
from sqlObjects.SqlValidator import sqlValidator
from outputInterface import finalQueryOutput

def createValidators(inputQuery):
    subQueries = subQuery.identifySubQueries(inputQuery)

    queryVariables = {}
    dynVar = 0
    diff = 0

    for k, v in subQueries.items():

        startIndex = int(k) - diff
        endIndex = int(v) - diff

        queryVariables[str(dynVar)] = sqlValidator(inputQuery[startIndex + 1:endIndex - 1])
        inputQuery = inputQuery.replace(inputQuery[startIndex:endIndex], '"{' + str(dynVar) + '}"', 1)

        diff += (v - k - 5)
        dynVar += 1

    queryStatements = {}

    for queryIndex, validator in queryVariables.items():
        queryStatements[queryIndex] = validator.query

    mainQuery = sqlValidator(inputQuery)
    mainQuery.query = removeExtraQuotes(mainQuery.query)
    mainQuery.updateParsed()

    finalQueryOutput(mainQuery, queryStatements)

def removeExtraQuotes(text):
    text = text.replace('"{', '({')
    text = text.replace('}"', '})')

    return text
