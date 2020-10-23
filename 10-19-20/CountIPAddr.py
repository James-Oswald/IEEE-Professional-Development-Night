
#https://www.codewars.com/kata/526989a41034285187000de4

def ipsBetween(ip1, ip2):
    p1 = [int(i) for i in ip1.split('.')]
    p2 = [int(i) for i in ip2.split('.')]
    diff = [p2[i] - p1[i] for i in range(0, 4)]
    rv = 0
    for i in range(0, 4):
        rv += pow(256, 3 - i) * diff[i]
    return rv

print(ipsBetween("10.0.0.0", "10.0.0.50"))
print(ipsBetween("10.0.0.0", "10.0.1.0")) 
print(ipsBetween("20.0.0.10", "20.0.1.0")) 