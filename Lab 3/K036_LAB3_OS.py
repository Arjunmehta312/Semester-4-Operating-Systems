#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sjf_scheduling():
    n = int(input("Enter number of processes: "))

    if n <= 0:
        print("Number of processes must be greater than 0.")
        return

    bt = []
    p = []
    wt = []
    tat = []

    print("\nEnter Burst Time for each process:")
    for i in range(n):
        burst_time = int(input(f"P{i+1}: "))
        bt.append(burst_time)
        p.append(i + 1)

    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if bt[j] < bt[pos]:
                pos = j
        bt[i], bt[pos] = bt[pos], bt[i]
        p[i], p[pos] = p[pos], p[i]

    print("\n\nk036 Arjun Mehta\n")

    wt.append(0)
    total_wt = 0

    for i in range(1, n):
        wt.append(sum(bt[:i]))
        total_wt += wt[i]

    avg_wt = total_wt / n

    total_tat = 0

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        tat.append(bt[i] + wt[i])
        total_tat += tat[i]
        print(f"P{p[i]}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    avg_tat = total_tat / n

    print(f"\nAverage Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")

sjf_scheduling()


# In[ ]:




