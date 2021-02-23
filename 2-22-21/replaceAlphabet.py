
def alphabet_position_max(seq):
    rv = ""
    for c in seq.upper():
        if(ord('A') <= ord(c) <= ord('Z')):
            rv += str(ord(c) - ord('A') + 1) + " "
    return rv[:-1]

alphabet_position=lambda t,s=0:" ".join([str(s) for c in t.upper() if 1<=(s:=ord(c)-64)<=26])

print(alphabet_position("The sunset sets at twelve o' clock."))