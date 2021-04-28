import validateQuotations as valQuotes
import validateTableAlias as valTableAlias

def runValidations(validator):
    valQuotes.checkQuotations(validator)
    valTableAlias.checkTableAlias(validator)
