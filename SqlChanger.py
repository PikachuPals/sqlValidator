class sqlResolver:

    def __init__(self, validator, change, reason):
        self.validator = validator
        self.change = change
        self.reason = reason





def underlineText(text):
    for index, char in text:
        text[index] = "\u0332".join(char)
    
    return text
