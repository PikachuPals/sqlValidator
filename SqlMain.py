import re
from SqlValidator import sqlValidator
from validatorCreator import createValidators

def queryIntake():
    query = input("Enter SQL Query: ")
    return query

inputQuery = queryIntake()

createValidators(inputQuery)

#SELECT SalesOrderID, LineTotal,(SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS AverageLineTotal, LineTotal - (SELECT AVG(LineTotal) FROM Sales.SalesOrderDetail) AS Variance FROM Sales.SalesOrderDetail
