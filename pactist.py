def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hallo(func):
    text = func("HI")
    print(text)



hallo(loud)