x = -125

epsilon = 0.01

numGuesses = 0

if x < 1:
    low = x
    high = 1

else:
    low = 0.0
    high = x

ans = (high + low) / 2.0

while abs(ans ** 3 - x) >= epsilon:
    print("low= " + str(low) + " high= " + str(high) + " ans= " + str(ans))
    numGuesses += 1

    if ans ** 3 < x:
        low = ans

    else:
        high = ans

    ans = (high + low) / 2.0

print("numGuesses= " + str(numGuesses))

print(str(ans) + 'is close to cube root of ' + str(x))