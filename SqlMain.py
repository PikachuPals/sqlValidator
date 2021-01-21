import re
from SqlValidator import sqlValidator

def queryIntake():
    query = input("Enter SQL Query: ")
    return query

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

inputQuery = queryIntake()
#test = sqlValidator(inputQuery)

subQueries = identifySubQueries(inputQuery)
print(subQueries)

queryVariables = {}
dynVar = 0
diff = 0

for k, v in subQueries.items():

    startIndex = int(k) - diff
    endIndex = int(v) - diff

    queryVariables[dynVar] = sqlValidator(inputQuery[startIndex:endIndex])    
    inputQuery = inputQuery.replace(inputQuery[startIndex:endIndex], "{" + str(dynVar) + "}", 1)
    
    diff += (v - k - 3)
    dynVar += 1

print(inputQuery) # Output altered query.

for query in range(0, len(queryVariables)):
    print(queryVariables.get(query).query) #Get query from object.

#SELECT SalesOrderID, LineTotal,(SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS AverageLineTotal, LineTotal - (SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS Variance FROM Sales.SalesOrderDetail
