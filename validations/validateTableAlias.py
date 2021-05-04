import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

from sqlObjects.SqlResolver import sqlResolver
from validations.Reasoning import reason

def checkTableAlias(validator):
    sqlTokens = validator.tokens

    tokenIndex = 0
    fromFlag = False

    for token in sqlTokens:

        # Capture only identifiers between from and where keywords.
        if token.ttype == sqlparse.tokens.Token.Keyword:
            if token.value.upper() == "FROM":
                fromFlag = True;

        elif isinstance(token, Where):
            fromFlag = False;
            return

        # Captures identifiers between from and where that have aliases.
        if fromFlag:
            if isinstance(token, Identifier) and token.is_group:
                for innerToken in sqlTokens:
                    if innerToken.ttype == sqlparse.tokens.Token.Keyword:
                        incorrectAlias(token, tokenIndex, validator)

            elif isinstance(token, IdentifierList):
                for innerIndex, identifier in enumerate(token.tokens):
                    if identifier.is_group:
                        for innerToken in sqlTokens:
                            if innerToken.ttype == sqlparse.tokens.Token.Keyword:
                                incorrectInnerAlias(identifier, tokenIndex, innerIndex, validator)

        tokenIndex += 1

def incorrectAlias(token, tokenIndex, validator):
    tokenValue = token.value

    aliasRegex = re.compile(" as ", re.IGNORECASE)
    aliasMatch = re.search(aliasRegex, tokenValue)

    # If as is found do the statements
    if aliasMatch is not None:
        # Replace as with space
        tokenValue = aliasRegex.sub(" ", tokenValue)
        resolver = sqlResolver(validator, tokenIndex, tokenValue, reason["tableAliasAs"])
        resolver.dynamicTokenChange()

def incorrectInnerAlias(token, tokenIndex, innerIndex, validator):
    tokenValue = token.value

    aliasRegex = re.compile(" as ", re.IGNORECASE)
    aliasMatch = re.search(aliasRegex, tokenValue)

    # If as is found do the statements
    if aliasMatch is not None:
        # Replace as with space
        tokenValue = aliasRegex.sub(" ", tokenValue)
        resolver = sqlResolver(validator, tokenIndex, tokenValue, reason["tableAliasAs"], innerIndex)
        resolver.dynamicTokenChange()
