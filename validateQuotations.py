import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import Identifier, IdentifierList, Where
import re

import SqlTokens as retrieveTokens

def checkQuotations(sqlTokens):
    whereTokens = retrieveTokens.whereTokens(sqlTokens)
    idTokens = retrieveTokens.identifierTokens(sqlTokens)

    print(idTokens)
        
