firstDigit = int(input())
secondDigit = int(input())
thirdDigit = int(input())
lastDigit = int(input())

if (firstDigit == 8 or firstDigit == 9) and secondDigit == thirdDigit and (lastDigit == 8 or lastDigit == 9):
    print("ignore")
else:
    print("answer")