import sqlparse
from sqlparse.tokens import *
import re

import SqlTokens as retrieveTokens
import validateQuotations as valQuotes

class sqlValidator:

    def __init__(self, statement):
        self.query = statement
        self.tokens = self.queryTokens()

        self.validate()

    def queryTokens(self):
        parsed = sqlparse.parse(self.query)[0]
        tokens = parsed.tokens

        return tokens

    def validate(self):
        valQuotes.checkQuotations(self.tokens)
