# AI-DeadLock-Detection
# AI-Based Deadlock Detection System

## Overview
This project implements an advanced AI-based deadlock detection system using Python, Tkinter for GUI, and NetworkX for graph-based deadlock detection. The system allows users to add multiple processes and resources, detect deadlocks, suggest resolutions, and generate automatic deadlock scenarios.

## Features
- **GUI-based Deadlock Detection**
- **Multiple Process and Resource Handling**
- **Graph Visualization** using NetworkX & Matplotlib
- **Auto-Generated Deadlock Scenarios**
- **Deadlock Resolution Suggestion**
- **Graph Reset Functionality**

---
## Installation
Ensure you have the following dependencies installed:

```bash
pip install networkx matplotlib tkinter
```

---
## How It Works
### Step 1: Start the Application
Run the script using Python:
```bash
python ai_deadlock_gui.py
```

### Step 2: Add Edges
- Enter **processes** and **resources** (comma-separated)
- Choose whether the edge represents **allocation (R→P) or request (P→R)**
- Click `Add Edge` to update the graph

### Step 3: Detect Deadlock
- Click `Detect Deadlock`
- If a cycle is detected, a warning will appear
- If no deadlock is found, a confirmation message appears

### Step 4: Auto-Generate Deadlock
- Click `Auto Generate Deadlock`
- This adds multiple processes and resources in a predefined deadlock scenario
- Check the visualization

### Step 5: Resolve Deadlock
- Click `Suggest Resolution`
- The system suggests terminating a process involved in the deadlock cycle

### Step 6: Reset Graph
- Click `Reset Graph` to clear the system and restart

---
## Diagram Representation
```
P1 → R1 → P2 → R2 → P3 → R3
                  ↑          ↓
               P5 ← R5 ← P4
```
- **Processes (P1, P2, P3, P4, P5)** represent system tasks
- **Resources (R1, R2, R3, R4, R5)** represent shared system resources
- **Arrows (→)** indicate resource requests or allocations
- **Deadlocks** occur when a cycle forms

---
## Future Enhancements
- Implement AI-based deadlock prediction
- Integrate logging and analytics for deadlock trends
- Extend with a distributed system deadlock detection

---
## License
This project is open-source under the MIT License.

![image](https://github.com/user-attachments/assets/0fb5c895-cc0d-4f46-a557-be9654deae6a)

