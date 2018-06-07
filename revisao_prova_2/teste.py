s = input()

for x in range(0, len(s)):
    if x == len(s) - 1:
        print (s[x])
    else:
        print (s[x], end='_')