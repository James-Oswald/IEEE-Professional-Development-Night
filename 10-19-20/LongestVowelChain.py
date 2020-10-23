
#https://www.codewars.com/kata/59c5f4e9d751df43cf000035

def longestVowelChain(inputString):
    chainLen = 0
    maxChainLen = 0
    for char in inputString:
        if char in ['a', 'e', 'i', 'o', 'u']:
            chainLen = chainLen + 1
            if chainLen > maxChainLen:
                maxChainLen = chainLen
        else:
            chainLen = 0
    return maxChainLen

print(longestVowelChain("codewarriors"))
print(longestVowelChain("aaaa"))