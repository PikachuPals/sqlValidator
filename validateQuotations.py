import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

import SqlTokens as retrieveTokens
from SqlResolver import sqlResolver
from Reasoning import reason

def checkQuotations(validator):
    sqlTokens = validator.tokens

    # Iterate to where and find incorrect tokens.
    tokenIndex = 0

    for token in sqlTokens:

        if token.ttype == sqlparse.tokens.Token.Literal.String.Single:
            misQuotedSelectIdentifier(token, tokenIndex, validator)

        elif isinstance(token, IdentifierList):
            for innerIndex, identifier in enumerate(token.tokens):
                if identifier.ttype == sqlparse.tokens.Token.Literal.String.Single:
                    misQuotedInnerIdentifier(identifier, tokenIndex, innerIndex, validator)

        tokenIndex += 1

def misQuotedSelectIdentifier(token, tokenIndex, validator):
    tokenString = token.value

    if tokenString.startswith("'") and tokenString.endswith("'"):
        tokenString = '"' + tokenString[1: -1] + '"'

        resolver = sqlResolver(validator, tokenIndex, tokenString, reason["misQuotedSelectIdentifier"])
        resolver.rootChange()


def misQuotedInnerIdentifier(token, tokenIndex, innerIndex, validator):
    tokenString = token.value

    if tokenString.startswith("'") and tokenString.endswith("'"):
        tokenString = '"' + tokenString[1: -1] + '"'

        resolver = sqlResolver(validator, tokenIndex, tokenString, reason["misQuotedSelectIdentifier"], innerIndex)
        resolver.innerTokenRootChange()



def misQuotedAlias(token, tokenIndex, validator):
    aliasRegex = r"(?i)(?<=as )(.+$)"

    aliasMatch = re.search(aliasRegex, token.value)
    alias = aliasMatch.group(0)

    if alias.startswith("'") and alias.endswith("'"):
        alias = '"' + alias[1: -1] + '"'

        return sqlResolver(validator, tokenIndex, alias, reason["misQuotedAlias"])

    elif " " in alias:
        if not alias.startswith('"') or alias.endswith('"'):
            alias = '"' + alias + '"'

            return sqlResolver(validator, tokenIndex, alias, reason["aliasMissingQuotes"])
    pass


# TODO Check entire string, then generate correct alias and identifier.
