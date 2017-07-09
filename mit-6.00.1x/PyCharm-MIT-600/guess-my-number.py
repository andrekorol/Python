print("Please think of a number between 0 and 100!")

low = 0
medium = 50
high = 100

print("Is your secret number %d?" % medium)

ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter "
            "'c' to indicate I guessed correctly.")
while True:
    if ans == 'h':
        high = medium
        medium = int((medium + low) / 2)

    elif ans == 'l':
        low = medium
        medium = int((medium + high) / 2)

    elif ans == 'c':
        break

    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number %d?" % medium)

    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter "
                "'c' to indicate I guessed correctly.")

print("Game over. Your secret number was: %d" % medium)
