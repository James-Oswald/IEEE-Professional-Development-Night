

def thirt(num):
    seq = [1, 10, 9, 12, 3, 4]
    s = sum([int(str(num)[i]) * seq[i % 6] for i in range(len(str(num)))])
    