year = input("Please Input The year :")
year = int(year)

if year % 400 == 0:
    print("Yes, It is a Leap Year")
elif year % 100 == 0:
    print("No, It is not a Leap Year")
elif year % 4 == 0:
    print("Yes, It is a Leap Year")
else:
    print("No, It is not a Leap Year")