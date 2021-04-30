import re

from sqlObjects.validatorCreator import createValidators
from config import cmdLine

def queryIntake():
    query = input("\nEnter 'q' to quit.\nEnter SQL Query: ")
    return query

def cmdLineInput():
    inputQuery = queryIntake()

    while inputQuery != "q":
        createValidators(inputQuery)
        inputQuery = queryIntake()

if __name__ == "__main__":
    if cmdLine:
        cmdLineInput()

#SELECT SalesOrderID, LineTotal,(SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS AverageLineTotal, LineTotal - (SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS Variance FROM Sales.SalesOrderDetail
