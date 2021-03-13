
#https://www.codewars.com/kata/5208f99aee097e6552000148

def solution1(s):
    rv = ""
    for i in range(len(s)-1):
        rv += s[i]
        if "A" < s[i+1] < "Z":
            rv += " "
    return rv + s[-1]

solution2 = lambda s:"".join([str(s[i])+(" "if"A"<s[i+1]<"Z"else"")for i in range(len(s)-1)]+[s[-1]])

print(solution2("camelCasing"))
print(solution2("caAMlCasinG"))
print(solution2("camelcasingtest"))