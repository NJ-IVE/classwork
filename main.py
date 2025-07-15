def is_leap(year):
    leap = False
    #nested if

    if year%4 ==0 and year%100 !=0 or year%400 ==0:
     print(year,"is a leap year")

    else:
     print(year,"is not a leap year")

    return leap

year = int(input("Enter year: "))
print(is_leap(year))