# the josephus problem
import math


def lives(n, s):
    if math.log(n, 2) == int(math.log(n, 2)):
        # print("{0} is power of 2".format(n))
        return s
    nearest_pow_of_2 = int(math.log(n, 2))
    # print("nearest power of 2:", nearest_pow_of_2)
    diff = n - (2**nearest_pow_of_2)
    # print("difference from {0} is :".format(n), diff)
    position = s + 2*diff
    # print("thus, position is:", position)
    if position > n:
        return position%n
    return position


persons = int(input("Enter number of persons: "))
start = int(input("Enter the start position: "))
if persons >= start :
    alive = lives(persons, start)
    print("Position number {0} lives!".format(alive))
else:
    print("Start position must be less than or equals to number of persons.")