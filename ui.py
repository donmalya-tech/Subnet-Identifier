import tkinter as tk
from tkinter import ttk


class SubnetUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Subnet Calculator")
        self.root.geometry("700x500")

        self.mode = tk.StringVar(value="prefix")

        self.build_inputs()
        self.build_buttons()
        self.build_output()

    def build_inputs(self):
        frame = ttk.LabelFrame(self.root, text="Input")
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame, text="IP Address:").grid(row=0, column=0, padx=5, pady=5)
        self.ip_entry = ttk.Entry(frame)
        self.ip_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Prefix (/):").grid(row=0, column=2)
        self.prefix_entry = ttk.Entry(frame, width=5)
        self.prefix_entry.grid(row=0, column=3)

        ttk.Label(frame, text="New Prefix / Hosts:").grid(row=1, column=0)
        self.value_entry = ttk.Entry(frame)
        self.value_entry.grid(row=1, column=1)

        ttk.Radiobutton(frame, text="By Prefix", variable=self.mode, value="prefix").grid(row=1, column=2)
        ttk.Radiobutton(frame, text="By Hosts", variable=self.mode, value="hosts").grid(row=1, column=3)

    def build_buttons(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="x", padx=10)

        self.info_btn = ttk.Button(frame, text="Subnet Info")
        self.info_btn.pack(side="left", padx=5)

        self.calc_btn = ttk.Button(frame, text="Calculate Subnets")
        self.calc_btn.pack(side="left", padx=5)

        self.export_btn = ttk.Button(frame, text="Export CSV")
        self.export_btn.pack(side="left", padx=5)

    def build_output(self):
        frame = ttk.LabelFrame(self.root, text="Output")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(frame, show="tree")
        self.tree.pack(fill="both", expand=True)
