processes = ["P1", "P2", "P3", "P4", "P5"]

arrival_time = [3, 0, 2, 1, 4]
burst_time = [4, 4, 3, 6, 2]
priority = [2, 0, 1, 1, 3]

n = len(processes)

remaining_time = burst_time.copy()
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
done = [False] * n

time = 0
completed = 0
gantt = []

while completed < n:
    idx = -1
    highest_priority = -1

    for i in range(n):
        if arrival_time[i] <= time and not done[i] and remaining_time[i] > 0:
            if priority[i] > highest_priority:
                highest_priority = priority[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    if not gantt or gantt[-1][0] != processes[idx]:
        gantt.append([processes[idx], time, time + 1])
    else:
        gantt[-1][2] = time + 1

    remaining_time[idx] -= 1
    time += 1

    if remaining_time[idx] == 0:
        done[idx] = True
        completed += 1
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

print("P\tAT\tBT\tPR\tCT\tTAT\tWT")

for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")

print("\nGantt Chart:")

for g in gantt:
    print(f"{g[0]}({g[1]}-{g[2]})", end=" ")
