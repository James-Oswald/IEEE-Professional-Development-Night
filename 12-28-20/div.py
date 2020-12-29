
#https://www.codewars.com/kata/564057bc348c7200bd0000ff

def thirtMax(num):
    seq = [1, 10, 9, 12, 3, 4]
    result = sum([int(str(num)[::-1][i]) * seq[i % 6] for i in range(len(str(num)))])
    return num if num == result else thirt(result)

thirt = lambda num, res=0: num if num == (res := sum([int(str(num)[::-1][i]) * [1, 10, 9, 12, 3, 4][i % 6] for i in range(len(str(num)))])) else thirt(res)

print(thirt(1234567))
print(thirt(321))