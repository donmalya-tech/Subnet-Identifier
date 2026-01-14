from tkinter import messagebox, filedialog
from subnet_logic import (
    subnet_extra_info,
    calculate_subnets,
    calculate_subnets_by_hosts,
    export_subnets_to_csv,
    validate_ip_and_prefix
)


class SubnetController:
    def __init__(self, ui):
        self.ui = ui
        self.results = []

        ui.info_btn.config(command=self.show_info)
        ui.calc_btn.config(command=self.calculate)
        ui.export_btn.config(command=self.export_csv)
    
    def show_info(self):
        ip = self.ui.ip_entry.get().strip()
        prefix_text = self.ui.prefix_entry.get().strip()

        if not ip or not prefix_text:
            messagebox.showerror("Input Error", "IP and prefix are required")
            return

        if not prefix_text.isdigit():
            messagebox.showerror("Input Error", "Prefix must be a number")
            return

        if not validate_ip_and_prefix(ip, prefix_text):
            messagebox.showerror("Input Error", "Invalid IP or prefix")
            return

        info = subnet_extra_info(ip, int(prefix_text))
        self.ui.tree.delete(*self.ui.tree.get_children())

        for k, v in info.items():
            self.ui.tree.insert("", "end", text=f"{k}: {v}")


    def calculate(self):
        ip = self.ui.ip_entry.get().strip()
        prefix_text = self.ui.prefix_entry.get().strip()
        value_text = self.ui.value_entry.get().strip()

        if not ip or not prefix_text or not value_text:
            messagebox.showerror("Input Error", "All fields are required")
            return

        if not prefix_text.isdigit() or not value_text.isdigit():
            messagebox.showerror("Input Error", "Prefix and Hosts must be numbers")
            return

        prefix = int(prefix_text)
        value = int(value_text)

        try:
            if self.ui.mode.get() == "prefix":
                self.results = calculate_subnets(ip, prefix, value)
            else:
                self.results = calculate_subnets_by_hosts(ip, prefix, value)

            self.ui.tree.delete(*self.ui.tree.get_children())

            for subnet in self.results:
                parent = self.ui.tree.insert("", "end", text=subnet["Subnet"])
                for k, v in subnet.items():
                    if k != "Subnet":
                        self.ui.tree.insert(parent, "end", text=f"{k}: {v}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def export_csv(self):
        if not self.results:
            messagebox.showwarning("Warning", "No data to export")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if filename:
            export_subnets_to_csv(self.results, filename)
            messagebox.showinfo("Success", "CSV exported successfully")
