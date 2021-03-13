
#https://www.codewars.com/kata/51e0007c1f9378fa810002a9

def deadfish1(s):
    v = 0
    rv = []
    for c in s:
        if c == 'i':
            v += 1
        elif c == 'd':
            v -= 1
        elif c == 's':
            v *= v
        elif c == 'o':
            rv.append(v)
    return rv

deadfish2 = lambda s,rv=0,v=0:rv if(rv:=[])or[(v:={"i":lambda:v+1,"d":lambda:v-1,"s":lambda:v*v,"o":lambda:v if rv.append(v) or 1 else-1}[c]()) for c in s]else-1


def deadfish3(s, rv=[], v=0):
    rv = []
    for c in s:
        v = {
            "i":lambda:v+1,
            "d":lambda:v-1,
            "s":lambda:v*v,
            "o":lambda:v if rv.append(v) else-1
        }[c]()
    return rv

print(deadfish2("iiisdoso"))
print(deadfish2("iiisdosodddddiso"))