import sqlparse
from sqlparse.tokens import *
from sqlparse.sql import *
import re

from sqlObjects.SqlResolver import sqlResolver
from validations.Reasoning import reason

def checkQuotations(validator):
    sqlTokens = validator.tokens

    # Iterate to where and find incorrect tokens.
    tokenIndex = 0

    for token in sqlTokens:

        # Misquoted Identifiers appear as string literals.
        if token.ttype == sqlparse.tokens.Token.Literal.String.Single:
            misQuotedSelectIdentifier(token, tokenIndex, validator)

        # If multiple identifiers, tokens get collected into an identifier list.
        elif isinstance(token, IdentifierList):
            for innerIndex, identifier in enumerate(token.tokens):
                if identifier.ttype == sqlparse.tokens.Token.Literal.String.Single:
                    misQuotedInnerIdentifier(identifier, tokenIndex, innerIndex, validator)

                elif isinstance(identifier, Identifier):
                    if identifier.is_group:
                        misQuotedAlias(identifier, tokenIndex, validator, innerIndex)

        elif isinstance(token, Identifier):
            if token.is_group:
                misQuotedAlias(token, tokenIndex, validator)

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

def misQuotedAlias(token, tokenIndex, validator, innerIndex = None):
    tokenValue = token.value

    # Regex to find words after as.
    aliasRegex = r"(?i)(?<= as )(.+$)"
    aliasMatch = re.search(aliasRegex, tokenValue)

    # If it finds a match.
    if aliasMatch is not None:
        indices = aliasMatch.span()
        alias = aliasMatch.group(0)

        # Correct the wrong quotations.
        if alias.startswith("'") and alias.endswith("'"):
            alias = '"' + alias[1: -1] + '"'
            tokenValue = tokenValue[:indices[0]] + alias + tokenValue[indices[1]:]

            resolver = sqlResolver(validator, tokenIndex, tokenValue, reason["misQuotedAlias"], innerIndex)
            resolver.dynamicTokenChange()

        elif " " in alias:
            if not alias.startswith('"') or alias.endswith('"'):
                alias = '"' + alias + '"'
                tokenValue = tokenValue[:indices[0]] + alias + tokenValue[indices[1]:]

                resolver = sqlResolver(validator, tokenIndex, tokenValue, reason["aliasMissingQuotes"], innerIndex)
                resolver.dynamicTokenChange()

    # Regex to find identifiers.
    identifierRegex = r"(?i)(.+)(?= as )"
    identifierMatch = re.search(identifierRegex, tokenValue)

    if identifierMatch is not None:
        indices = identifierMatch.span()
        identifier = identifierMatch.group(0)

        if identifier.startswith("'") and identifier.endswith("'"):
            identifier = '"' + identifier[1: -1] + '"'
            tokenValue = tokenValue[:indices[0]] + identifier + tokenValue[indices[1]:]

            resolver = sqlResolver(validator, tokenIndex, tokenValue, reason["misQuotedSelectIdentifier"], innerIndex)
            resolver.dynamicTokenChange()
