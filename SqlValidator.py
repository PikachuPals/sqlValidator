import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import Identifier, IdentifierList, Where

import SqlTokens as retrieveTokens

def queryIntake():
    query = input("Enter SQL Query: ");
    return query

def queryTokens(query):
    parsed = sqlparse.parse(query)[0]
    tokens = parsed.tokens
    
    return tokens

def checkStrings(tokens):
    whereTokens = retrieveTokens.whereTokens(tokens)


def checkColumns(tokens):
    idTokens = retrieveTokens.identifierTokens(tokens)


tokens = queryTokens(queryIntake())
checkStrings(tokens)
