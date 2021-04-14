import sqlparse
from sqlparse.tokens import *
import re

import SqlTokens as retrieveTokens
import validateQuotations as valQuotes

class sqlValidator:

    def __init__(self, statement):
        self.query = statement
        self.parsed = sqlparse.parse(self.query)[0]
        self.tokens = self.parsed.tokens

        self.validate()


    def validate(self):
        valQuotes.checkQuotations(self)

    def getTokens(self):
        return self.tokens

    def getParsed(self):
        return self.parsed

    def alterQuery(self, tokenIndex, newToken):
        self.parsed.tokens[tokenIndex] = newToken
        self.query = str(self.parsed)
