def faces(string):
    string = str(string)
    words = string.split(" ")
    string2 = ""
    for word in words:
        if word == ":)":
            word = "\U0001F600"
        if word == ":(":
            word = "\U0001F614"
        word += " "
        string2 += "".join(word)
        
    return string2
        
    
        
    
