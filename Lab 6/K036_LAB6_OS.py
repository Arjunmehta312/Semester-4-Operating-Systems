#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dataclasses import dataclass
from typing import List
from queue import PriorityQueue
import heapq
from datetime import datetime

# System Information
CURRENT_TIME = "2025-02-14 08:58:25"
CURRENT_USER = "Arjunmehta312"

@dataclass
class Process:
    pid: int
    priority: int
    burst_time: int
    arrival_time: int
    remaining_time: int = None
    completion_time: int = 0
    waiting_time: int = 0
    turnaround_time: int = 0
    
    def __post_init__(self):
        self.remaining_time = self.burst_time if self.remaining_time is None else self.remaining_time
    
    def __lt__(self, other):
        return self.priority < other.priority

class PriorityScheduler:
    def __init__(self, is_preemptive=False):
        self.processes = []
        self.is_preemptive = is_preemptive
        self.current_time = 0
        print(f"\nSystem Info:\nTime: {CURRENT_TIME}\nUser: {CURRENT_USER}")
    
    def add_process(self, pid, priority, burst_time, arrival_time):
        self.processes.append(Process(pid, priority, burst_time, arrival_time))
    
    def non_preemptive_schedule(self):
        processes = sorted(self.processes, key=lambda x: x.arrival_time)
        ready_queue = PriorityQueue()
        completed = []
        time = 0
        i = 0
        
        while len(completed) < len(processes):
            while i < len(processes) and processes[i].arrival_time <= time:
                ready_queue.put((processes[i].priority, processes[i]))
                i += 1
                
            if ready_queue.empty():
                time += 1
                continue
                
            _, process = ready_queue.get()
            process.waiting_time = time - process.arrival_time
            time += process.burst_time
            process.completion_time = time
            process.turnaround_time = process.completion_time - process.arrival_time
            completed.append(process)
            
        return completed
    
    def preemptive_schedule(self):
        processes = [Process(
            p.pid, p.priority, p.burst_time, p.arrival_time, p.burst_time
        ) for p in self.processes]
        ready_queue = []
        completed = []
        time = 0
        i = 0
        
        while len(completed) < len(processes):
            while i < len(processes) and processes[i].arrival_time <= time:
                heapq.heappush(ready_queue, (processes[i].priority, i, processes[i]))
                i += 1
                
            if not ready_queue:
                time += 1
                continue
                
            _, _, process = heapq.heappop(ready_queue)
            process.remaining_time -= 1
            time += 1
            
            if process.remaining_time > 0:
                heapq.heappush(ready_queue, (process.priority, i, process))
            else:
                process.completion_time = time
                process.turnaround_time = time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed.append(process)
                
        return completed
    
    def schedule(self):
        completed = (self.preemptive_schedule() if self.is_preemptive 
                    else self.non_preemptive_schedule())
        
        print(f"\n{'Preemptive' if self.is_preemptive else 'Non-Preemptive'} Priority Scheduling:")
        print("PID Priority Burst Arrival Completion Waiting Turnaround")
        print("-" * 60)
        
        total_waiting = total_turnaround = 0
        for p in completed:
            print(f"{p.pid:3d} {p.priority:8d} {p.burst_time:5d} {p.arrival_time:7d} "
                  f"{p.completion_time:10d} {p.waiting_time:7d} {p.turnaround_time:10d}")
            total_waiting += p.waiting_time
            total_turnaround += p.turnaround_time
            
        n = len(completed)
        print(f"\nAverage Waiting Time: {total_waiting/n:.2f}")
        print(f"Average Turnaround Time: {total_turnaround/n:.2f}")
        return completed

# Example usage
def main():
    # Test processes
    processes = [
        (1, 3, 6, 0),  # (pid, priority, burst_time, arrival_time)
        (2, 1, 4, 1),
        (3, 4, 2, 2),
        (4, 2, 3, 3)
    ]
    
    # Non-preemptive scheduling
    non_preemptive = PriorityScheduler(is_preemptive=False)
    for pid, priority, burst, arrival in processes:
        non_preemptive.add_process(pid, priority, burst, arrival)
    non_preemptive.schedule()
    
    # Preemptive scheduling
    preemptive = PriorityScheduler(is_preemptive=True)
    for pid, priority, burst, arrival in processes:
        preemptive.add_process(pid, priority, burst, arrival)
    preemptive.schedule()

if __name__ == "__main__":
    main()

