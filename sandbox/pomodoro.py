#!/usr/bin/env python3.6
# -*-coding: utf-8-*-
import time
import sys


# Defining the main function
def pomodoro(a, set_time, rest_time, sets, beep_time):
    # Defining the counter function
    def counter(timer, remaining_string):
        timer_in_sec = timer * 60
        for remaining in range(timer_in_sec, 0, -1):
            sys.stdout.write("\r")
            if remaining > 60:
                minutes = remaining // 60
                sec = remaining - (minutes * 60)
                if sec < 10:
                    sys.stdout.write("%d:0%d remaining %s" % (minutes, sec, remaining_string))
                else:
                    sys.stdout.write("%d:%d remaining %s" % (minutes, sec, remaining_string))
                sys.stdout.flush()
                time.sleep(1)
            else:
                sys.stdout.write("{:2d} seconds remaining %s".format(remaining) % remaining_string)
                sys.stdout.flush()
                time.sleep(1)
        sys.stdout.write("\rComplete!            \n")

    if a == 0:
        print("Do you wish to start the Pomodoro timer?")

        input("If your answer is yes press <ENTER>. If you wish to "
              "close the program press CTRL-c")

        set_time = int(input("Enter how many minutes you wish your timer to be:\n"))
        rest_time = int(input("Enter how many minutes you wish your break to take:\n"))
        sets = int(input("Enter how many sets you're willing to go for: \n"))
        beep_time = int(input("Enter how many seconds you wish the beep to sound for:\n"))
        set_num = 1
        set_string = "until the end of the set n° %d" % set_num
        rest_string = "until the end of the rest of %d minute(s)" % rest_time
        checkmarks = 0
    while checkmarks < sets:
        print("Starting set n° %d now!" % set_num)
        counter(set_time, set_string)
        for i in range(beep_time):
            print(chr(7))
            time.sleep(1)
            print(chr(27) + "[2J")
        checkmarks += 1
        print("Congratulations! Set %d done!" % set_num)
        if set_num < sets:
            input("Now press <ENTER> to start the break timer or press CTRL-c to finish the program")
            set_string = "until the end of the set n° %d" % set_num
            counter(rest_time, rest_string)
            set_num += 1
            for i in range(beep_time):
                print(chr(7))
                time.sleep(1)
                print(chr(27) + "[2J")
            if set_num == sets:
                break
            answer = input("Press <ENTER> to start the next set, press CTRL-c to exit the program or type and enter "
                           "\"restart\" to restart the program: \n")
            if answer == "":
                continue
            elif answer == "restart":
                pomodoro(0, None, None, None, None)

    print("You have finished %d set(s) of %d minutes." % (sets, set_time))
    print("Congratulations on your hard work and dedication! Keep up the good work!")
    while True:
        answer_2 = input("Do you want to start the Pomodoro timer again with the same configurations? [y/n]: ")
        if not answer_2 == "y" or "Y" or "yes" or "YES" or "Yes" or "YEs" or "yES" or "n" or "N" or "NO" \
                or "No" or "nO" or "no":
            print("Your answer is not valid. Please type y or n")
            continue
        else:
            break
    if answer_2 == "y" or "Y" or "yes" or "YES" or "Yes" or "YEs" or "yES":
        pomodoro(1, set_time, rest_time, sets, beep_time)
    elif answer_2 == "n" or "N" or "NO" or "No" or "nO" or "no":
        while True:
            answer_3 = input("Type \"q\" if you want to close the program or type \"r\" if you want to restart:\n")
            if not answer_3 == "q" or "Q" or "r" or "R":
                print("Your answer is not valid. Please type q or r")
                continue
            else:
                break
        if answer_3 == "q" or "Q":
            sys.exit(1)
        elif answer_3 == "r" or "R":
            pomodoro(0, None, None, None, None)
    else:
        pomodoro(1, set_time, rest_time, sets, beep_time)


pomodoro(0, None, None, None, None)
