import validations.validateQuotations as valQuotes
import validations.validateTableAlias as valTableAlias

def runValidations(validator):
    valQuotes.checkQuotations(validator)
    valTableAlias.checkTableAlias(validator)

    # Append more validations in this method.
