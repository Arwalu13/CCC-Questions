currentLn = input("")

while currentLn != "TTYL":
    if currentLn == "CU":
        print("see you")

    elif currentLn == ":-)":
        print("I'm happy")

    elif currentLn == ":-(":
        print("I'm unhappy")
    
    elif currentLn == ";-)":
        print("wink")

    elif currentLn == ":-P":
        print("stick out my tongue")

    elif currentLn == "(~.~)":
        print("sleepy")

    elif currentLn == "TA":
        print("totally awesome")

    elif currentLn == "CCC":
        print("Canadian Computing Competition")

    elif currentLn == "CUZ":
        print("because")

    elif currentLn == "TY":
        print("thank you")

    elif currentLn == "YW":
        print("you're welcome")
    
    else:
        print(currentLn)
    
    currentLn = input("")

print("talk to you later")