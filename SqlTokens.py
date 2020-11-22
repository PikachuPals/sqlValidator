import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import Identifier, IdentifierList, Where

def identifierTokens(tokens):
    idTokens = []
    
    for token in tokens:
        if isinstance(token, Identifier):
            idTokens.append(token)
        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                idTokens.append(identifier)
            
    return idTokens

def whereTokens(tokens):
    whereTokens = []

    for token in tokens:
        if isinstance(token, Where):
            whereTokens.append(token)

    return whereTokens
