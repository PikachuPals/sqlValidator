import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

import SqlTokens as retrieveTokens
from SqlResolver import sqlResolver
from Reasoning import reason

def checkQuotations(validator):
    sqlTokens = validator.tokens

    # Iterate to where and find wrong identifiers.
    tokenIndex = 0

    for token in sqlTokens:

        if isinstance(token, Where):

            for innerToken in token:
                if isinstance(innerToken, Comparison):
                    resolver = misQuotedSelectIdentifier(token.tokens[0], tokenIndex, validator)

                    if resolver is not None:
                        resolver.whereLeftChange()

            tokenIndex += 1

        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                resolver = misQuotedSelectIdentifier(identifier, tokenIndex, validator)

                if resolver is not None:
                    resolver.topLevelChange()

                if identifier.has_alias():
                    resolver = misQuotedAlias(token.tokens[0], tokenIndex, validator)
                    if resolver is not None:
                        resolver.aliasChange()

        else:
            resolver = misQuotedSelectIdentifier(token, tokenIndex, validator)
            if resolver is not None:
                resolver.topLevelChange()

        tokenIndex += 1

def misQuotedSelectIdentifier(token, tokenIndex, validator):
    tokenString = token.value

    if tokenString.startswith("'") and tokenString.endswith("'"):
        tokenString = '"' + tokenString[1: -1] + '"'

        return sqlResolver(validator, tokenIndex, tokenString, reason["misQuotedSelectIdentifier"])

    else:
        return None

def misQuotedAlias(token, tokenIndex, validator):
    aliasRegex = r"(?i)(?<=as )(.+$)"

    aliasMatch = re.match(aliasRegex, token)
    alias = aliasMatch.group(0)

    if alias.startswith("'") and alias.endswith("'"):
        alias = '"' + alias[1: -1] + '"'

        return sqlResolver(validator, tokenIndex, alias, reason["misQuotedAlias"])

    elif " " in alias:
        if not alias.startswith('"') or alias.endswith('"'):
            alias = '"' + alias + '"'

            return sqlResolver(validator, tokenIndex, alias, reason["aliasMissingQuotes"])
    pass
