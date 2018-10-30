number = int(
    input("What number to you want to calculate the square root for? "))
possible_sqrt = 1

tolerance = 0.00001

while (possible_sqrt * possible_sqrt - number) > tolerance or (
        possible_sqrt * possible_sqrt - number) < -tolerance:
    print("possible_sqrt", possible_sqrt)
    possible_sqrt = (possible_sqrt + (number / possible_sqrt)) / 2

print("The square root of", number, "is", possible_sqrt)
