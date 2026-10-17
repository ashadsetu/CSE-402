
pages = [1, 2, 3, 4, 5, 1, 2, 3, 1]
capacity = 3

# FIFO
print("===== FIFO =====")
frames = []
faults = 0
hits = 0

for page in pages:
    if page not in frames:
        faults += 1

        if len(frames) < capacity:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
    else:
        hits += 1

    print("Page:", page, "Frames:", frames)

total = len(pages)
fault_ratio = faults / total
hit_ratio = hits / total
fault_hit_ratio = faults / hits if hits != 0 else 0

print("Total Faults:", faults)
print("Total Hits:", hits)
print("Page fault ratio:", fault_ratio)
print("Page hit ratio:", hit_ratio)
print("Fault to hit ratio:", fault_hit_ratio)


# MRU
print("\n===== MRU =====")
frames = []
faults = 0
hits = 0

for page in pages:
    if page not in frames:
        faults += 1

        if len(frames) < capacity:
            frames.append(page)
        else:
            frames.pop(-1)
            frames.append(page)
    else:
        hits += 1
        frames.remove(page)
        frames.append(page)

    print("Page:", page, "Frames:", frames)

total = len(pages)
fault_ratio = faults / total
hit_ratio = hits / total
fault_hit_ratio = faults / hits if hits != 0 else 0

print("Total Faults:", faults)
print("Total Hits:", hits)
print("Page fault ratio:", fault_ratio)
print("Page hit ratio:", hit_ratio)
print("Fault to hit ratio:", fault_hit_ratio)
