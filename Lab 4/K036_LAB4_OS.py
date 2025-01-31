#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import deque


# In[3]:


def round_robin(processes, time_quantum):
    processes = sorted(processes, key=lambda x: x['arrival_time'])
    queue = deque()
    current_time = 0
    next_process = 0
    total_tat = 0
    total_wt = 0

    # Initialize remaining_time for all processes
    for p in processes:
        p['remaining_time'] = p['burst_time']
        p['completion_time'] = None

    # Add initial processes to the queue
    while next_process < len(processes) and processes[next_process]['arrival_time'] <= current_time:
        queue.append(processes[next_process])
        next_process += 1

    while queue:
        current_process = queue.popleft()
        execute_time = min(time_quantum, current_process['remaining_time'])
        current_time += execute_time
        current_process['remaining_time'] -= execute_time

        # Add newly arrived processes to the queue
        while next_process < len(processes) and processes[next_process]['arrival_time'] <= current_time:
            queue.append(processes[next_process])
            next_process += 1

        if current_process['remaining_time'] == 0:
            current_process['completion_time'] = current_time
            tat = current_process['completion_time'] - current_process['arrival_time']
            wt = tat - current_process['burst_time']
            total_tat += tat
            total_wt += wt
        else:
            queue.append(current_process)

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)
    return avg_tat, avg_wt


# In[5]:


print("Arjun Mehta")
print("K021")

processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 1},
    {'pid': 'P4', 'arrival_time': 3, 'burst_time': 2},
    {'pid': 'P5', 'arrival_time': 4, 'burst_time': 3},
]

time_quantum = 2
avg_tat, avg_wt = round_robin(processes, time_quantum)

print("Process | Completion Time | Turnaround Time | Waiting Time")
for p in processes:
    tat = p['completion_time'] - p['arrival_time']
    wt = tat - p['burst_time']
    print(f"{p['pid']}      | {p['completion_time']:15} | {tat:15} | {wt:12}")

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")


# In[ ]:




