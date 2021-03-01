import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re
import outputInterface as OI

import SqlTokens as retrieveTokens

def checkQuotations(sqlTokens):
    whereTokens = retrieveTokens.whereTokens(sqlTokens)
    idTokens = retrieveTokens.identifierTokens(sqlTokens)

    for token in whereTokens:
        if isinstance(token, Comparison):
            checkIdentifiers(token.tokens[0])
        

def checkIdentifiers(identifier):

    if identifier.value.startswith("'") and identifier.value.endswith("'"):
        return False
    else:
        return True
    
    
