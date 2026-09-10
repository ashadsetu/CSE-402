pid = ["P1", "P2", "P3", "P4"]
AT = [0, 3, 1, 2]
BT = [3, 2, 2, 1]
PT = [4, 0, 2, 1]
n = 4

completed = [False] * n
CT = [0] * n
TAT = [0] * n
WT = [0] * n

time = 0
finished = 0
sequence = []

while finished < n:
    idx = -1
    min_priority = 9999

    for i in range(n):
        if not completed[i] and AT[i] <= time:
            if PT[i] < min_priority:
                min_priority = PT[i]
                idx = i

    if idx == -1:
        time += 1
    else:
        time += BT[idx]
        CT[idx] = time
        completed[idx] = True
        finished += 1
        sequence.append(pid[idx])

for i in range(n):
    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]

print("\n\nPriority Scheduling Non-Preemptive")
print("Process\tAT\tBT\tPT\tCT\tTAT\tWT")

for i in range(n):
    print(f"{pid[i]}\t{AT[i]}\t{BT[i]}\t{PT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

avg_wt_priority = sum(WT) / n
avg_tat_priority = sum(TAT) / n

print("\nAverage Waiting Time =", avg_wt_priority)
print("Average Turnaround Time =", avg_tat_priority)

print("\nExecution Sequence:")
print(" -> ".join(sequence))
