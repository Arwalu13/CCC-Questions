firstNum = int(input())
secondNum = int(input())

answer = 0

for i in range(firstNum, secondNum + 1):
    if len([j for j in range(1, i + 1) if not i % j]) == 4:
        answer += 1

print(f"The number of RSA numbers between {firstNum} and {secondNum} is {answer}")