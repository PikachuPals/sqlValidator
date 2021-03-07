import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

import outputInterface as OI
import SqlTokens as retrieveTokens
from Reasoning import reason

def checkQuotations(validator):
    sqlTokens = validator.tokens

    # Iterate to where and find wrong identifiers.
    idTokens = []

    for token in sqlTokens:
        if isinstance(token, Where):
            break
        
        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                misQuotedSelectIdentifier(identifier)
                
            idTokens.append(identifier)
            
        else:
            misQuotedSelectIdentifier(token)    
    
    whereTokens = retrieveTokens.whereTokens(sqlTokens)


    for token in whereTokens:
        if isinstance(token, Comparison):
            misQuotedSelectIdentifier(token.tokens[0])
       

def misQuotedSelectIdentifier(token):
    tokenString = token.value
    if tokenString.startswith("'") and tokenString.endswith("'"):
        OI.cmdLineOutput(tokenString, "test", reason["misQuotedSelectIdentifier"])

    
    
