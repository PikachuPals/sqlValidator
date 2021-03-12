import sqlparse
from sqlparse.tokens import *
import re

import SqlTokens as retrieveTokens
import validateQuotations as valQuotes

class sqlValidator:

    def __init__(self, statement, subquery = False):
        self.query = statement
        self.subquery = subquery
        self.parsed = sqlparse.parse(self.query)[0]
        self.tokens = self.parsed.tokens

        self.validate()


    def validate(self):
        valQuotes.checkQuotations(self)

    def checkMultiColumn(self):
        return False

    def alterQuery(self, tokenIndex, newToken):
        self.parsed.tokens[tokenIndex] = newToken
        
        
