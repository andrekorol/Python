def trexcept():
    try:
        b = int(input("Tell me one number\n"))
        c = int(input("Tell me another number\n"))
        print(b/c)
        print("Okay")

    except ValueError:
        print("Could not convert the input to a number.")
        trexcept()

    except ZeroDivisionError:
        print("Can't divide by zero.")
        trexcept()

    except:
        print("Something went very wrong.")
        trexcept()

trexcept()