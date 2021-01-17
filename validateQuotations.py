import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import Identifier, IdentifierList, Where
import re

import SqlTokens as retrieveTokens

def checkQuotations(sql):
    whereTokens = retrieveTokens.whereTokens(sql.tokens)
    idTokens = retrieveTokens.identifierTokens(sql.tokens)

    parenthesisRgx = r"\([\w]+\)"

    for idToken in idTokens:
        print(idToken)
        
