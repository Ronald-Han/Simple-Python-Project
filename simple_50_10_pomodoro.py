import time

WORK = 50 * 60
BREAK = 10 * 60

print("Simple 50/10 Pomodoro (Ctrl+C to Pause/Resume)")

while True:
    for label, duration in [("Work", WORK), ("Break", BREAK)]:
        remaining = duration
        print(f"\n{label} Time Started!")
        while remaining > 0:
            try:
                print(f"\r{label} Time Left: {remaining//60:02d}:{remaining%60:02d}", end="")
                time.sleep(1)
                remaining -= 1
            except KeyboardInterrupt:
                input("\nPaused. Press ENTER to resume.")
        print(f"\n{label} session finished!")
