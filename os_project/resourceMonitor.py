import psutil
import time

def monitor_cpu_usage(interval = 1):
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=interval)
            print(f"CPU Usage: {cpu_percent}%")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    print("Resource Management - CPU Usage Monitor")
    print("1. Start CPU Usage Monitoring")
    print("2. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        monitor_cpu_usage()
    elif choice == "2":
        pass  # The program will exit naturally
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()