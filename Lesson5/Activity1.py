num1 = [1, 2, 3, 4]
num2 = [8, 9, 10, 11]
res = map(lambda x, y: x + y, num1, num2)
print("Sum of 2 lists:", (list(res)))
num3 = [1, 2, 3, 4, 5, 6]
def se(n):
    return n*n
sq = list(map(se, num3))
print("Square of numbers:", sq)


