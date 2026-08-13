pid = ["p4", "p2", "p1", "p3", "p5"]
AT = [1, 2, 3, 4, 5]
BT = [2, 4, 5, 3, 3]

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

print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for i in range(5):
    print(f"{pid[i]:<5}{AT[i]:<5}{BT[i]:<5}{CT[i]:<5}{TAT[i]:<5}{WT[i]:<5}")

avg_tat = sum(TAT) / 5
avg_wt = sum(WT) / 5

print("\nAverage TAT =", avg_tat)
print("Average WT =", avg_wt)

print("\nExecution Sequence:")
for i in range(5):
    print(pid[i], end=" ")
