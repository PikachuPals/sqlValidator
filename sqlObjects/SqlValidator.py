import sqlparse
from sqlparse.tokens import *
import re

import SqlTokens as retrieveTokens
import validations.validationManager as valManager

class sqlValidator:

    def __init__(self, statement):
        self.query = statement
        self.parsed = sqlparse.parse(self.query)[0]
        self.tokens = self.parsed.tokens

        self.validate()

    def validate(self):
        valManager.runValidations(self)

    def getTokens(self):
        return self.tokens

    # Returns a new parsed object to avoid overwriting old parsed object.
    def getParsed(self):
        return sqlparse.parse(self.query)[0]

    def alterQuery(self, tokenIndex, newToken):
        self.parsed.tokens[tokenIndex] = newToken
        self.query = str(self.parsed)

    def alterQueryInnerToken(self, tokenIndex, innerIndex, newToken):
        self.parsed.tokens[tokenIndex].tokens[innerIndex] = newToken
        self.query = str(self.parsed)

    def updateParsed(self):
        self.parsed = sqlparse.parse(self.query)[0]
