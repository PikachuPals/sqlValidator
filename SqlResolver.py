import outputInterface as OI
import sqlparse
import os

os.system("")

class sqlResolver:

    def __init__(self, validator, tokenIndex, change, reason, innerIndex = None):

        self.validator = validator
        self.tokenIndex = tokenIndex

        self.change = change
        self.reason = reason

        self.innerIndex = innerIndex

    # Function to change a token on parse.
    def rootChange(self):
        placeholderParse = self.validator.getParsed()
        errorInStatement = underlineText(placeholderParse.tokens[self.tokenIndex].value)
        placeholderParse.tokens[self.tokenIndex].value = errorInStatement

        if OI.cmdLineOutput(placeholderParse, self.change, self.reason):
            newToken = sqlparse.parse(self.change)[0].tokens[0]
            self.validator.alterQuery(self.tokenIndex, newToken)

    # Function to change a token in a token list.
    def innerTokenRootChange(self):
        placeholderParse = self.validator.getParsed()

        # Underline error in text and parse into tokens.
        errorInStatement = underlineText(placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value)

        # Rewrite old token with newer token.
        placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value = errorInStatement

        if OI.cmdLineOutput(placeholderParse, self.change, self.reason):
            newInnerToken = sqlparse.parse(self.change)[0].tokens[0]
            self.validator.getParsed().tokens[self.tokenIndex].tokens[self.innerIndex]
            self.validator.alterQueryInnerToken(self.tokenIndex, self.innerIndex, newInnerToken)

    def innerTokenChange(self):
        pass

    def whereLeftChange(self):
        newString = underlineText(validator.tokens[self.tokenIndex].value)
        newToken = sqlparse.parse(newString)[0].tokens[0]

        validator.alterQuery(self.tokenIndex, newToken)

        OI.cmdLineOutput(validator.parsed, change, self.reason)

    def whereRightChange(self):
        return None

def underlineText(text):
    return u"\u001b[4m" + text + "\u001b[0m"
