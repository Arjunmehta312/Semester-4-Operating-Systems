#!/usr/bin/env python
# coding: utf-8

# In[3]:


# List of processes with (Process ID, Burst Time)
processes = [(1, 5), (2, 3), (3, 8), (4, 6)]
 
# Initialize waiting time and turnaround time lists
waiting_time = [0] * len(processes)
turnaround_time = [0] * len(processes)
 
# Calculate waiting time
for i in range(1, len(processes)):
    waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]
 
# Calculate turnaround time
for i in range(len(processes)):
    turnaround_time[i] = processes[i][1] + waiting_time[i]
 
# Print the results
print("Process | Waiting Time | Turnaround Time")
for i in range(len(processes)):
    print(f"{processes[i][0]}       | {waiting_time[i]}          | {turnaround_time[i]}")


# In[ ]:





# In[ ]:




