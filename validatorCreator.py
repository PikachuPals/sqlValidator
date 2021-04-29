import subQueryLookUp as subQuery
from SqlValidator import sqlValidator

def createValidators(inputQuery):
    subQueries = subQuery.identifySubQueries(inputQuery)

    queryVariables = {}
    dynVar = 0
    diff = 0

    for k, v in subQueries.items():

        startIndex = int(k) - diff
        endIndex = int(v) - diff

        queryVariables[dynVar] = sqlValidator(inputQuery[startIndex + 1:endIndex - 1])
        inputQuery = inputQuery.replace(inputQuery[startIndex:endIndex], '"{"' + str(dynVar) + '"}"', dynVar)

        diff += (v - k - 5)
        dynVar += 1

    queryStatements = {}

    for queryIndex, validator in queryVariables.items():
        queryStatements[queryIndex] = validator.query

    mainQuery = sqlValidator(inputQuery)

    print(mainQuery.query.format(**queryStatements))
