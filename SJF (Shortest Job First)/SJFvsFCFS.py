# SJF
pid = ["P1", "P2", "P3", "P4", "P5"]
AT = [2,3,0,1,1]
BT = [5,1,2,3,6]

n = 5
completed = [False] * n
CT = [0] * n
TAT = [0] * n
WT = [0] * n

time = 0
finished = 0
sequence = []

while finished < n:
    idx = -1
    min_bt = 9999

    for i in range(n):
        if not completed[i] and AT[i] <= time:
            if BT[i] < min_bt:
                min_bt = BT[i]
                idx = i

    if idx == -1:
        time = time + 1
    else:
        time = time + BT[idx]
        CT[idx] = time
        completed[idx] = True
        finished = finished + 1
        sequence.append(pid[idx])

for i in range(n):
    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]

avg_tat_sjf = sum(TAT) / n
avg_wt_sjf = sum(WT) / n

print("========== SJF ==========")
print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for i in range(n):
    print(f"{pid[i]:<5}{AT[i]:<5}{BT[i]:<5}{CT[i]:<5}{TAT[i]:<5}{WT[i]:<5}")

print("\nAverage TAT =", avg_tat_sjf)
print("Average WT =", avg_wt_sjf)

print("\nExecution Sequence:")
print(" -> ".join(sequence))

# FCFS
pid = ["p3","p4","p5","p1","p2"]
AT = [1,2,3,4,5]
BT = [2,3,6,5,1]


CT = []
TAT = []
WT = []

ct = 0

for i in range(5):
    if ct < AT[i]:
        ct = AT[i]

    ct = ct + BT[i]
    CT.append(ct)

for i in range(5):
    tat = CT[i] - AT[i]
    TAT.append(tat)

    wt = tat - BT[i]
    WT.append(wt)

avg_tat_fcfs = sum(TAT) / 5
avg_wt_fcfs = sum(WT) / 5

print("\n========== FCFS ==========")
print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for i in range(5):
    print(f"{pid[i]:<5}{AT[i]:<5}{BT[i]:<5}{CT[i]:<5}{TAT[i]:<5}{WT[i]:<5}")

print("\nAverage TAT =", avg_tat_fcfs)
print("Average WT =", avg_wt_fcfs)

print("\nExecution Sequence:")
print(" -> ".join(pid))

# Comparison
print("\n========== Comparison ==========")

print(f"{'Algorithm':<12}{'Avg TAT':<12}{'Avg WT':<12}")
print(f"{'SJF':<12}{avg_tat_sjf:<12.2f}{avg_wt_sjf:<12.2f}")
print(f"{'FCFS':<12}{avg_tat_fcfs:<12.2f}{avg_wt_fcfs:<12.2f}")

if avg_wt_sjf < avg_wt_fcfs:
    print("\nSJF gives lower average waiting time, so SJF is better for this data set.")
else:
    print("\nFCFS gives lower average waiting time, so FCFS is better for this data set.")
