import time
import winsound

def alert():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def focus_timer(total_time, focus_interval, break_interval):
    while True:
        print("Focus for {} minutes".format(focus_interval))
        time.sleep(focus_interval * 60)
        alert()

        print("Take a break for {} minutes".format(break_interval))
        time.sleep(break_interval * 60)
        alert()

if __name__ == "__main__":
    total_time = 60  # Total time in minutes
    focus_interval = 25  # Focus interval in minutes
    break_interval = 5  # Break interval in minutes

    focus_timer(total_time, focus_interval, break_interval)
