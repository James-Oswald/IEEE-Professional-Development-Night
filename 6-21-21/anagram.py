
#https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def genDict(w):
    rv = {}
    for c in w:
        if c in rv.keys():
            rv[c] += 1
        else:
            rv[c] = 1
    return rv
  
def anagrams(word, words):
    wordDict = genDict(word)
    print(wordDict)
    rv = []
    for altword in words:
        print(genDict(altword))
        if wordDict == genDict(altword):
            rv.append(altword)
    return rv