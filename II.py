for i in range(50, 90, 10): # range(start, stop, intervals)
    print(i, end=' ')

def check(num: float) -> None:
    if num <= 50.0:
        print("Has Passed")
    else:
        print("Has not Passed")
    return

def check_two(num: float) -> bool:
    if num<=50:
        return True
    else:
        return False

check(89.9)
check_two(45.7)

has_passed: bool = check_two(30.2)
print(has_passed)


def calculate_area(radius: float)-> float:

    return 22/7 * (radius ** 2)

print(calculate_area(7.0))

def sumation(b: float, y: float)-> float:
    return b+y
def sumation_II(b: float, y: float)-> float:
    return b+y
def sumation_III(b: float, y: float)-> float:
    return b+y

print(sumation(3,5))