import threading

# Define resources and processes
resources = ['R1', 'R2', 'R3']
processes = ['P1', 'P2', 'P3']

# Define the allocation matrix and request matrix
allocation = {
    'P1': {'R1': 1, 'R2': 0, 'R3': 1},
    'P2': {'R1': 0, 'R2': 1, 'R3': 0},
    'P3': {'R1': 1, 'R2': 1, 'R3': 0},
}

request = {
    'P1': {'R1': 0, 'R2': 1, 'R3': 0},
    'P2': {'R1': 0, 'R2': 0, 'R3': 1},
    'P3': {'R1': 1, 'R2': 0, 'R3': 0},
}

# Define a function to check for deadlock
def check_deadlock():
    while True:
        deadlock = True
        for process in processes:
            if process not in finished_processes:
                can_allocate = True
                for resource in resources:
                    if request[process][resource] > available[resource]:
                        can_allocate = False
                        break
                if can_allocate:
                    for resource in resources:
                        available[resource] += allocation[process][resource]
                    finished_processes.append(process)
                    deadlock = False
        if deadlock:
            print("\nDeadlock detected!")
            break

# Initialize available resources
available = {
    'R1': 1,
    'R2': 1,
    'R3': 1,
}

finished_processes = []

# Create threads to check for deadlock
deadlock_thread = threading.Thread(target=check_deadlock)

# Start the deadlock detection thread
deadlock_thread.start()

# Simulate resource allocation and release
while True:
    print("\nChoose an action:")
    print("1. Allocate resources")
    print("2. Release resources")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        process = input("Enter the process (e.g., P1): ")
        resource = input("Enter the resource (e.g., R1): ")
        amount = int(input("Enter the amount to allocate: "))
        if process in processes and resource in resources and amount >= 0:
            if amount <= available[resource]:
                allocation[process][resource] += amount
                available[resource] -= amount
                print(f"Allocated {amount} units of {resource} to {process}.")
            else:
                print(f"Not enough {resource} resources available.")
        else:
            print("Invalid process or resource.")

    elif choice == '2':
        process = input("Enter the process (e.g., P1): ")
        resource = input("Enter the resource (e.g., R1): ")
        amount = int(input("Enter the amount to release: "))
        if process in processes and resource in resources and amount >= 0:
            if amount <= allocation[process][resource]:
                allocation[process][resource] -= amount
                available[resource] += amount
                print(f"Released {amount} units of {resource} from {process}.")
            else:
                print(f"{process} does not have {amount} units of {resource} allocated.")
        else:
            print("Invalid process or resource.")

    elif choice == '3':
        break

# Wait for the deadlock detection thread to finish
deadlock_thread.join()

print("Simulation complete.")