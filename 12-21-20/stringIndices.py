
def solve(string, index):
    counter = 0
    if string[index] != "(":
        return -1
    for i in range(index + 1, len(string)):
        if counter == 0 and string[i] == ")":
            return i
        elif string[i] == "(":
            counter += 1
        elif string[i] == ")":
            counter -= 1
    return -1

print(solve("((1)23(45))(aB)", 0)) # 10 #the opening brace at index 0 matches the closing brace at index 10
print(solve("((1)23(45))(aB)", 1)) #= 3 
print(solve("((1)23(45))(aB)", 2)) #= -1 #there is no opening bracket at index 2, so return -1
print(solve("((1)23(45))(aB)", 6)) #= 9
print(solve("((1)23(45))(aB)", 11)) #= 14
print(solve("((>)|?(*'))(yZ)", 11)) #= 14