import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

import SqlTokens as retrieveTokens
from SqlResolver import sqlResolver
from Reasoning import reason

def checkQuotations(validator):
    sqlTokens = validator.tokens

    # Iterate to where and find wrong identifiers.
    tokenIndex = 0

    for token in sqlTokens:
        
        if isinstance(token, Where):
            
            for innerToken in token:
                if isinstance(innerToken, Comparison):
                    resolver = misQuotedSelectIdentifier(token.tokens[0], tokenIndex, validator)
                    if resolver is not None:
                        resolver.whereLeftChange()
                    
            tokenIndex += 1
        
        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                misQuotedSelectIdentifier(identifier)
             
        else:
            misQuotedSelectIdentifier(token, tokenIndex, validator)

        tokenIndex += 1 

def misQuotedSelectIdentifier(token, tokenIndex, validator):
    tokenString = token.value
    
    if tokenString.startswith("'") and tokenString.endswith("'"):
        tokenString = '"' + tokenString[1: -1] + '"'
        
        return sqlResolver(validator, tokenIndex, tokenString, reason["misQuotedSelectIdentifier"])

    else:
        return None
    
    
    
