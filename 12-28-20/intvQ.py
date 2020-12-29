

#https://www.codewars.com/kata/5b358a1e228d316283001892

def appr(string):
    string = string.lower().replace(" ", "")
    d={}
    for char in string:
        if d.get(char) == None:
            d[char] = 1
        else:
            d[char] += 1
    rv = ""
    for key in d.keys():
        rv += key + ":" + ("*" * d[key]) + ","
    return rv[:-1]

print(appr("Chicago"))
print(appr("Bangkok"))
print(appr("Las Vegas"))