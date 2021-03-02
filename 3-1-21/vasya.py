
# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def canGiveChange(payments):
    curBills = {25: 0, 50: 0, 100: 0}
    for payment in payments:
        change = payment - 25    #the amount of change we need to make
        curBills[payment] += 1   #another bill in our register
        while change != 0:                              #Can we make change? If yes this loop will exit
            if change >= 50 and curBills[50] > 0:       #They need >= 50 and we have a 50
                curBills[50] -= 1
                change -= 50
            elif change >= 25 and curBills[25] > 0:     #They need >= 25 and we have a 25
                curBills[25] -= 1
                change -= 25
            else:                                       #We can't make change
                return "NO"
    return "YES"                                        

print(canGiveChange([25, 25, 50])) #Yes
print(canGiveChange([25, 100]))  #No
print(canGiveChange([25, 25, 50, 50, 100])) #No