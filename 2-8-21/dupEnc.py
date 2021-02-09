
def dupenc(inputString):
    s = inputString.lower()
    rv = ""
    for i in range(len(s)):
        flag = False
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                flag = True
                break
        if flag:            #The char has appeared multiple times
            rv += ")"
        else:               #The char has only appeared once
            rv += "("
    return rv

print(dupenc("din"))        #"((("
print(dupenc("recede"))     #"()()()"
print(dupenc("Success"))    #")())())"
print(dupenc("(( @"))       #"))((" 