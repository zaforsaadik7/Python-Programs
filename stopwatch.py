import time
def stopwatch(seconds):
    for i in range (seconds, 0, -1):
        print(f"{i} second{'s' if i!=1 else ' '} left.")
        time.sleep(1)
    print("Time's Up!")

countdown_time= int(input('Enter the countdown time in seconds:'))
stopwatch(countdown_time)
