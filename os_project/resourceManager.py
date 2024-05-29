from itertools import permutations
print()
print()
class ResourceManager:
    def __init__(self, num_resources):
        self.num_resources = num_resources
        self.resources = [0] * num_resources
        self.available = [0] * num_resources
        self.max_resources = {}
        self.allocated_resources = {}

    def request_resources(self, process_id, requested):
        if all(requested[i] <= self.available[i] for i in range(self.num_resources)):
            for i in range(self.num_resources):
                self.available[i] -= requested[i]
                self.allocated_resources[process_id][i] += requested[i]
            return True
        return False

    def release_resources(self, process_id):
        for i in range(self.num_resources):
            self.available[i] += self.allocated_resources[process_id][i]
            self.allocated_resources[process_id][i] = 0

    def add_process(self, process_id, max_claim):
        self.max_resources[process_id] = max_claim
        self.allocated_resources[process_id] = [0] * self.num_resources

def is_safety_sequence(manager, sequence):
    work = manager.available.copy()
    finish = {pid: False for pid in manager.max_resources.keys()}

    for pid in sequence:
        if all(manager.allocated_resources[pid][i] + work[i] >= manager.max_resources[pid][i] for i in range(manager.num_resources)):
            work = [work[i] + manager.allocated_resources[pid][i] for i in range(manager.num_resources)]
            finish[pid] = True
        else:
            return False

    return all(finish.values())

def find_safe_sequence(manager):
    processes = list(manager.max_resources.keys())
    for sequence in permutations(processes):
        if is_safety_sequence(manager, sequence):
            return sequence
    return None

def main():
    num_resources = 3
    manager = ResourceManager(num_resources)

    manager.resources = [10, 5, 7]
    manager.available = [10, 5, 7]

    manager.add_process("P1", [7, 5, 3])
    manager.add_process("P2", [3, 2, 2])
    manager.add_process("P3", [9, 0, 2])
    manager.add_process("P4", [2, 2, 2])
    manager.add_process("P5", [4, 3, 3])

    request_sequence = [
        ("P1", [0, 1, 0]),
        ("P2", [2, 0, 0]),
        ("P3", [3, 0, 2]),
        ("P4", [2, 1, 1]),
        ("P5", [0, 0, 2]),
    ]

    for pid, request in request_sequence:
        if manager.request_resources(pid, request):
            print(f"Request by {pid} for {request} granted.")
            safe_sequence = find_safe_sequence(manager)
            if safe_sequence:
                print(f"System is in a safe state. Safe sequence: {safe_sequence}\n")
            else:
                print("System is not in a safe state.\n")
        else:
            print(f"Request by {pid} for {request} denied.\n")

        manager.release_resources(pid)

if __name__ == "__main__":
    main()