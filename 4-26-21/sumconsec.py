
#https://www.codewars.com/kata/55eeddff3f64c954c2000059

def sumConsec(arr):
    rv = []
    cur = None
    summ = 0
    for num in arr:
        if num == cur:
            summ += num
        else:
            if cur != None:
                rv.append(summ)
                summ = 0
            cur = num
            summ += num
    rv.append(summ)
    return rv

print(sumConsec([1,4,4,4,0,4,3,3,1])) #[1,12,0,4,6,1]
print(sumConsec([1,1,7,7,3]))          #[2,14,3]
print(sumConsec([-5,-5,7,7,12,0]))      # [-10,14,12,0]