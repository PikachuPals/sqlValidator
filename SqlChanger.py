def underlineText(text):
    for index, char in text:
        text[index] = "\u0332".join(char)
    
    return text
