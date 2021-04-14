import outputInterface as OI
import sqlparse
import os

os.system("")

class sqlResolver:

    def __init__(self, validator, tokenIndex, change, reason):

        self.validator = validator
        self.tokenIndex = tokenIndex

        self.change = change
        self.reason = reason

    def topLevelChange(self):
        placeholderParse = self.validator.getParsed()
        errorInStatement = underlineText(placeholderParse.tokens[self.tokenIndex].value)
        placeholderParse.tokens[self.tokenIndex].value = errorInStatement

        if OI.cmdLineOutput(placeholderParse, self.change, self.reason):
            newToken = sqlparse.parse(self.change)[0].tokens[0]
            self.validator.alterQuery(self.tokenIndex, newToken)

    def whereLeftChange(self):
        newString = underlineText(validator.tokens[self.tokenIndex].value)
        newToken = sqlparse.parse(newString)[0].tokens[0]

        validator.alterQuery(self.tokenIndex, newToken)

        OI.cmdLineOutput(validator.parsed, change, self.reason)

    def whereRightChange(self):
        return None

def underlineText(text):
    return u"\u001b[4m" + text + "\u001b[0m"
