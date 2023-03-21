import tkinter as tk
import threading
import requests
from tkinter import messagebox

class StressTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("Stress Test")

        # IP address input
        self.ip_label = tk.Label(master, text="IP Address:")
        self.ip_label.grid(row=0, column=0)
        self.ip_entry = tk.Entry(master, width=30)
        self.ip_entry.grid(row=0, column=1)

        # Virtual user input
        self.users_label = tk.Label(master, text="Virtual Users:")
        self.users_label.grid(row=1, column=0)
        self.users_entry = tk.Entry(master, width=30)
        self.users_entry.grid(row=1, column=1)

        # Time input
        self.time_label = tk.Label(master, text="Time (seconds):")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(master, width=30)
        self.time_entry.grid(row=2, column=1)

        # Run button
        self.run_button = tk.Button(master, text="Run Test", command=self.run_test)
        self.run_button.grid(row=3, column=1)

    def run_test(self):
        ip = self.ip_entry.get()
        users = int(self.users_entry.get())
        time = int(self.time_entry.get())

        # Confirmation prompt
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to run the stress test?")
        if not confirm:
            return

        # Define the function for each thread
        def run_test_thread():
            for i in range(users):
                response = requests.get(ip)
                print(f"User {i+1} got response {response.status_code}")

        # Start the threads
        threads = []
        for i in range(users):
            thread = threading.Thread(target=run_test_thread)
            thread.start()
            threads.append(thread)

        # Wait for specified time
        for thread in threads:
            thread.join(timeout=time)

        print("Stress test complete.")

root = tk.Tk()
gui = StressTestGUI(root)
root.mainloop()
