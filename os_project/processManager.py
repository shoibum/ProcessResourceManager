import psutil

def list_processes():
    print("List of Running Processes:")
    for process in psutil.process_iter(attrs=["pid", "name"]):
        print(f"PID: {process.info['pid']} - Name: {process.info['name']}")

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} terminated.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"Permission denied to terminate PID {pid}.")
        
def main():
    while True:
        print("\nProcess Manager Menu:")
        print("1. List Running Processes")
        print("2. Kill a Process")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_processes()
        elif choice == "2":
            pid = int(input("Enter the PID of the process to kill: "))
            kill_process(pid)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()