import time
import sys


def counter(timer, remaining_string):
    timer_in_sec = timer * 60
    for remaining in range(timer_in_sec, 0, -1):
        sys.stdout.write("\r")
        if remaining > 60:
            min = remaining // 60
            sec = remaining - (min * 60)
            if sec < 10:
                sys.stdout.write("%d:0%d remaining %s" % (min, sec, remaining_string))
            else:
                sys.stdout.write("%d:%d remaining %s" % (min, sec, remaining_string))
            sys.stdout.flush()
            time.sleep(1)
        else:
            sys.stdout.write("{:2d} seconds remaining %s".format(remaining) % remaining_string)
            sys.stdout.flush()
            time.sleep(1)
    sys.stdout.write("\rComplete!            \n")
counter(3, "until the end of the task")