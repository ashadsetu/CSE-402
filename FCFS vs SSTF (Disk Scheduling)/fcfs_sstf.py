Req = [0, 30, 41, 62, 14, 20]
head = 20

# FCFS

fcfs_req = Req.copy()
fcfs_head = head
fcfs_total = 0

if fcfs_head in fcfs_req:
    fcfs_req.remove(fcfs_head)

print("FCFS")
print("Seek Sequence:", fcfs_head, end="")

for i in fcfs_req:
    movement = abs(fcfs_head - i)
    fcfs_total += movement
    fcfs_head = i
    print(" >", i, end="")

print("\nTotal Head Movement:", fcfs_total)

# SSTF

sstf_req = Req.copy()
sstf_head = head
sstf_total = 0

if sstf_head in sstf_req:
    sstf_req.remove(sstf_head)

print("\nSSTF")
print("Seek Sequence:", sstf_head, end="")

while sstf_req:
    closest = min(sstf_req, key=lambda x: abs(x - sstf_head))
    movement = abs(sstf_head - closest)
    sstf_total += movement
    sstf_head = closest
    sstf_req.remove(closest)
    print(" >", closest, end="")

print("\nTotal Head Movement:", sstf_total)
```
