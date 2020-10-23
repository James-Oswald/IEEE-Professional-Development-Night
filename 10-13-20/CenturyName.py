
#https://www.codewars.com/kata/52fb87703c1351ebd200081f

#normal sane person version
def century(year):
    sufixs = ["th", "st", "nd", "rd"] + (["th"] * 6)
    cent = int(year) // 100 + 1
    return str(cent) + sufixs[cent % 10 if cent // 10 != 1 else 0]

#one liner
centurymin = lambda year: str(int(year) // 100 + 1) + (["th", "st", "nd", "rd"] + (["th"] * 6))[(int(year) // 100 + 1) % 10 if (int(year) // 100 + 1) // 10 != 1 else 0]


for i in range(0, 3000, 101):
    print(str(i) + " : " + centurymin(str(i)))