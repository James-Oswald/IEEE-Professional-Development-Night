
#https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python

def make_upper_case(s):
    rv = ""
    for c in s:
        if(ord("a") <= ord(c) <= ord("z")):
            rv += chr(ord(c) - 32)
        else:
            rv += c
    return rv    
       