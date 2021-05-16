import time

print ("Would you like a timer, or a countdown?")

timerOrCountdown = input()
TORC = timerOrCountdown.lower()


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(t)
        time.sleep(1)
        t -= 1


if TORC == "countdown":

    print("Please enter the length in seconds of the desired countdown:")
    countdownLength = input()
    countdown(int(countdownLength))

else:

    print("Welcome to the timer function.")
    input("Press enter to start: ")
    start_time = time.time()

    input("Press enter to stop: ")
    end_time = time.time()

    time_lapsed = end_time - start_time
    print(str(time_lapsed) + " seconds")




