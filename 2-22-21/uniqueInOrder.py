
def unique_in_order_max(seq):
    rv = []
    last = ''
    for i in range(len(seq)):
        if(seq[i] != last):
            rv.append(seq[i])
            last = seq[i]
    return rv

unique_in_order = lambda s,l='':[l:=s[i] for i in range(len(s)) if s[i]!=l]

print(unique_in_order('AAAABBBCCDAABBB')) #== ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))         #== ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1,2,2,3,3]))       #== [1, 2, 3]