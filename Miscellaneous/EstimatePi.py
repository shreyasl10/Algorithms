import random


def EstimatePi(n):
    circlePoints = 0
    squarePoints = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            circlePoints += 1
        squarePoints += 1
    return 4*(circlePoints/squarePoints)


n = int(input("Enter the no of points  "))
print(EstimatePi(n))
