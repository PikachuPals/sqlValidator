import outputInterface as OI
import sqlparse

class sqlResolver:

    def __init__(self, validator, tokenIndex, change, reason):

        self.validator = validator
        self.tokenIndex = tokenIndex

        self.change = change
        self.reason = reason

    def topLevelChange(self):
        newString = underlineText(validator.tokens[tokenIndex].value)
        newToken = sqlparse.parse(newString)[0].tokens[0]

        validator.alterQuery(tokenIndex, newToken)

        OI.cmdLineOutput(validator.parsed, change, reason)
        
    def whereLeftChange(self):
        return None

    def whereRightChange(self):
        return None

def underlineText(text):
    return "\u0332".join(text)
