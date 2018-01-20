def get_sets_names():
    while True:
        print("Enter a letter for the first set"
              "(uppercase only, lowercase letters will be set to uppercase): ")
        setAname = str(input()).upper()
        if len(setAname) != 1:
            print("Please enter only ONE letter.")
        else:
            print(f"\nOk, the first set will be called {setAname}")
            break

    while True:
        print("\nNow enter a letter for the second set"
              "(uppercase only, lowercase letters will be set to uppercase): ")
        setBname = str(input()).upper()
        if len(setBname) != 1:
            print("Please enter only ONE letter.")
        elif setBname == setAname:
            print(f"\n{setAname} is already the first set! "
                  "Please enter a different letter.")
        else:
            print(f"\nOk, the second set will be called {setBname}")
            break

    return setAname, setBname


def get_sets_elements(setAname, setBname):
    setA = []
    break_on = False
    while True:
        print(f"\nPlease enter the elements of the set {setAname}"
              "(real numbers only): ")
        try:
            setAfloats = [float(x) for x in input().split()]
            for y in setAfloats:
                if y == int(y) and int(y) not in setA:
                    setA.append(int(y))
                elif y not in setA:
                    setA.append(y)
            break_on = True
        except ValueError:
            print("\nOnly real numbers are accepted!")
        print(f"{setAname} = ", setA)
        if break_on and setA:
            break

    setB = []
    break_on = False
    while True:
        print(f"\nNow please enter the elements of the set {setBname}"
              "(real numbers only): ")
        try:
            setBfloats = [float(x) for x in input().split()]
            for y in setBfloats:
                if y == int(y) and int(y) not in setB:
                    setB.append(int(y))
                elif y not in setB:
                    setB.append(y)
            break_on = True
        except ValueError:
            print("\nOnly real numbers are accepted!")
        print(f"{setBname} = ", setB)
        if break_on and setB:
            break

    return setA, setB


def products_of_sets(setA, setB):
    P = []
    for b in setB:
        for a in setA:
            P.append((a, b))
    P.sort()

    return P


setAname, setBname = get_sets_names()
setA, setB = get_sets_elements(setAname, setBname)
P = products_of_sets(setA, setB)
print(P)
