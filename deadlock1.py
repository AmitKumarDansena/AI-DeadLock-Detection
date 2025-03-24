import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def detect_deadlock():
    global G
    try:
        cycles = list(nx.simple_cycles(G))
        if cycles:
            messagebox.showwarning("Deadlock Detected", f"Deadlock cycles found: {cycles}")
        else:
            messagebox.showinfo("No Deadlock", "No deadlock detected in the system.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def add_edge():
    processes = entry_process.get().strip().split(',')
    resources = entry_resource.get().strip().split(',')
    allocation = var_allocation.get()
    
    if processes and resources:
        for process in processes:
            for resource in resources:
                if allocation:
                    G.add_edge(resource.strip(), process.strip(), label="Allocated")
                else:
                    G.add_edge(process.strip(), resource.strip(), label="Requested")
        draw_graph()
    else:
        messagebox.showwarning("Input Error", "Process and Resource fields cannot be empty.")

def draw_graph():
    plt.clf()
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    canvas.draw()

def reset_graph():
    global G
    G.clear()
    draw_graph()

def auto_generate():
    global G
    G.clear()
    processes = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
    resources = ["R1", "R2", "R3", "R4", "R5"]
    edges = [("P1", "R1"), ("R1", "P2"), ("P2", "R2"), ("R2", "P3"), ("P3", "R3"), 
             ("R3", "P4"), ("P4", "R4"), ("R4", "P5"), ("P5", "R5"), ("R5", "P1")]
    
    for edge in edges:
        G.add_edge(*edge, label=random.choice(["Allocated", "Requested"]))
    draw_graph()

def suggest_resolution():
    global G
    try:
        cycles = list(nx.simple_cycles(G))
        if cycles:
            messagebox.showinfo("Resolution Suggestion", f"Terminate process: {cycles[0][0]} to resolve deadlock.")
        else:
            messagebox.showinfo("No Deadlock", "No resolution needed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Advanced AI-Based Deadlock Detection System")
G = nx.DiGraph()

tk.Label(root, text="Processes (comma-separated):").grid(row=0, column=0)
entry_process = tk.Entry(root)
entry_process.grid(row=0, column=1)

tk.Label(root, text="Resources (comma-separated):").grid(row=1, column=0)
entry_resource = tk.Entry(root)
entry_resource.grid(row=1, column=1)

var_allocation = tk.BooleanVar()
tk.Checkbutton(root, text="Allocation (Checked: R->P, Unchecked: P->R)", variable=var_allocation).grid(row=2, column=0, columnspan=2)

tk.Button(root, text="Add Edge", command=add_edge).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Detect Deadlock", command=detect_deadlock).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Suggest Resolution", command=suggest_resolution).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Reset Graph", command=reset_graph).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Auto Generate Deadlock", command=auto_generate).grid(row=7, column=0, columnspan=2)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=8, column=0, columnspan=2)

draw_graph()
root.mainloop()
