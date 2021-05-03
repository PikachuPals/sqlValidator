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

        if OI.output(placeholderParse, self.change, self.reason):
            newToken = sqlparse.parse(self.change)[0].tokens[0]
            self.validator.alterQuery(self.tokenIndex, newToken)

    # Function to change a token in a token list.
    def innerTokenRootChange(self):
        placeholderParse = self.validator.getParsed()

        # Underline error in text and parse into tokens.
        # Rewrite old token with newer token.
        errorInStatement = underlineText(placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value)
        placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value = errorInStatement

        # Checks if token contains tokens attribute, to underline all tokens rather than one.
        if hasattr(placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex], 'tokens'):
            errorInStatement = underlineTokenList(placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].tokens)
            placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].tokens = errorInStatement
        else:
            errorInStatement = underlineText(placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value)
            placeholderParse.tokens[self.tokenIndex].tokens[self.innerIndex].value = errorInStatement

        if OI.output(placeholderParse, self.change, self.reason):
            newInnerToken = sqlparse.parse(self.change)[0].tokens[0]
            self.validator.getParsed().tokens[self.tokenIndex].tokens[self.innerIndex]
            self.validator.alterQueryInnerToken(self.tokenIndex, self.innerIndex, newInnerToken)

    # Function to choose between token changes if innerIndex is set.
    def dynamicTokenChange(self):
        if self.innerIndex is not None:
            self.innerTokenRootChange()
        else:
            self.rootChange()

def underlineText(text):
    return u"\u001b[4m" + text + "\u001b[0m"

def underlineTokenList(tokenList):
    for token in tokenList:
        token.value = underlineText(token.value)

    return tokenList
