word = input()
answer = True

for i in range(len(word)):
    if not (word[i] == 'I' or word[i] == 'O' or word[i] == 'S' or word[i] == 'H' or word[i] == 'Z' or word[i] == 'X' or word[i] == 'N'):
        answer = False

if answer == True:
    print("YES")

else:
    print("NO")
