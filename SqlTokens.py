import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
from sqlparse import tokens as T

def identifierTokens(tokens):
    idTokens = []
    
    for token in tokens:
        if isinstance(token, Identifier):
            idTokens.append(token)
        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                idTokens.append(identifier)
        elif isinstance(token, Function):
            for identifier in Function.get_parameters(token):
                idTokens.append(identifier)
            
    return idTokens

def whereTokens(tokens):
    whereTokens = []

    for token in tokens:
        if isinstance(token, Where):
            whereTokens.append(token)
            
    if len(whereTokens) == 0:
        return whereTokens
    else:
        return whereTokens[0].tokens
