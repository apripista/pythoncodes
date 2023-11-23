import time


def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    return alarm_time


def main():
    print("Simple Alarm Clock")
    alarm_time = set_alarm()

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            break
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
