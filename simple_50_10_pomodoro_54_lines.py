import time

WORK_MIN = 50
BREAK_MIN = 10

WORK = WORK_MIN * 60
BREAK = BREAK_MIN * 60

print("Simple 50/10 Pomodoro Timer")
print("Press Ctrl+C to pause, ENTER to resume")

def countdown(label, seconds):
    remaining = seconds
    print(f"\n{label} session started!")
    while remaining > 0:
        try:
            mins = remaining // 60
            secs = remaining % 60
            print(f"\r{label} Time Left: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            remaining -= 1
        except KeyboardInterrupt:
            input("\nPaused. Press ENTER to continue.")
    print(f"\n{label} session finished!")

def start_pomodoro():
    while True:
        countdown("Work", WORK)
        countdown("Break", BREAK)

start_pomodoro()


