import time

def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins:02d}:{secs:02d}'
        print("⏳ Timer:", timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

# User input
try:
    total_time = int(input("Enter time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("❌ Please enter a valid number.")
