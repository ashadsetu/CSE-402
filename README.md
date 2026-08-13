# FCFS (First-Come, First-Served)

```text
 ██████╗ ███████╗███████╗     ██╗  ██╗ ██████╗ ██████╗
██╔════╝ ██╔════╝██╔════╝     ██║  ██║██╔═████╗╚════██╗
██║      ███████╗█████╗       ███████║██║██╔██║ █████╔╝
██║      ╚════██║██╔══╝       ╚════██║████╔╝██║██╔═══╝
╚██████╗ ███████║███████╗          ██║╚██████╔╝███████╗
 ╚═════╝ ╚══════╝╚══════╝          ╚═╝ ╚═════╝ ╚══════╝

              O P E R A T I N G   S Y S T E M
                         L A B
```

## FCFS Scheduling

**FCFS (First-Come, First-Served)** is a simple CPU scheduling algorithm where the process that arrives first is executed first.

### Features

* Non-preemptive scheduling algorithm
* Processes are executed in arrival order
* Simple and easy to implement
* Uses a FIFO (First-In, First-Out) approach

### Files

* `FCPS.py` — Python implementation of FCFS CPU scheduling.

### Scheduling Metrics

The program can calculate:

* **Completion Time (CT)**
* **Turnaround Time (TAT)**
* **Waiting Time (WT)**

### Formula

```text
Turnaround Time = Completion Time - Arrival Time

Waiting Time = Turnaround Time - Burst Time
```

### Example

```text
Process    Arrival Time    Burst Time
P1         0               5
P2         1               3
P3         2               2
```

Execution order:

```text
P1 → P2 → P3
```

---

**Course:** CSE-402
**Lab:** Operating System Lab
**Algorithm:** FCFS (First-Come, First-Served)
