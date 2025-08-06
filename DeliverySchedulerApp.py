import tkinter as tk # Import tkinter module as tk
from tkinter import ttk, messagebox # Import ttk and messagebox from tkinter module
from typing import List, Tuple # Import List and Tuple from typing module

class Task: # Represents a delivery task
    def __init__(self, id, processing_time, deadline): # id: Task ID, processing_time: Time required to process the task, deadline: Time by which the task should be completed
        self.id = id # Unique ID for the task
        self.processing_time = processing_time # Time required to process the task
        self.deadline = deadline # Time by which the task should be completed
        self.profit = self.calculate_profit() # Profit earned by completing the task
        self.profit_to_time_ratio = self.profit / self.processing_time # Profit earned per hour of processing time

    def calculate_profit(self): # Calculate profit earned by completing the task
        return self.processing_time * 10  # Profit = Processing Time * 10

    def get_profit_in_rupees(self): # Get profit in rupees
        return f"₨{self.profit}" # Format profit as rupees

def schedule_delivery_tasks(tasks: List[Task], num_vehicles: int) -> List[Tuple[int, int]]: # Schedule delivery tasks to vehicles
    tasks.sort(key=lambda x: x.deadline) # Sort tasks by deadline
    tasks.sort(key=lambda x: x.profit_to_time_ratio, reverse=True) # Sort tasks by profit-to-time ratio in descending order
    
    schedule = [] # List to store the schedule
    current_time = [0] * num_vehicles # List to store the current time for each vehicle
    
    # Schedule tasks to vehicles
    for task in tasks: # Iterate over each task
        for vehicle in range(num_vehicles): # Iterate over each vehicle
            if current_time[vehicle] + task.processing_time <= task.deadline: # Check if the task can be completed by the deadline
                schedule.append((task.id, vehicle)) # Add task to the schedule
                current_time[vehicle] += task.processing_time # Update current time for the vehicle
                break # Break the loop as the task has been scheduled
    
    return schedule # Return the schedule

class DeliverySchedulerApp: # Delivery Scheduler Application
    def __init__(self, root): # Initialize the application
        self.root = root # Root window
        self.root.title("Delivery Scheduler") # Set window title
        self.tasks = [] # List to store tasks
        self.last_task_id = 0  # Initialize the last task ID to 0
        self.create_widgets() # Create widgets
        
    def create_widgets(self): # Create widgets
        style = ttk.Style(self.root) # Style for the widgets
        style.theme_use('clam') # Set theme to 'clam'

        style.configure("TFrame", background="#2e2e2e") # Configure frame style
        style.configure("TLabel", background="#2e2e2e", foreground="white") # Configure label style
        style.configure("TEntry", fieldbackground="#3e3e3e", background="#2e2e2e", foreground="white") # Configure entry style
        style.configure("TButton", background="#4e4e4e", foreground="white", relief="flat", padding=10) # Configure button style
        style.map("TButton", background=[('active', '#3e3e3e')], foreground=[('active', 'white')]) # Configure button style
        style.configure("Treeview", background="#2e2e2e", fieldbackground="#3e3e3e", foreground="white") # Configure treeview style
        style.configure("Treeview.Heading", background="#3e3e3e", foreground="white") # Configure treeview heading style
        style.map("Treeview.Heading", background=[('active', '#2e2e2e')], foreground=[('active', 'white')]) # Configure treeview heading style

        self.task_frame = ttk.Frame(self.root, padding="10") # Frame to add tasks
        self.task_frame.grid(row=0, column=0, sticky=(tk.W, tk.E)) # Grid layout for the frame
        
        ttk.Label(self.task_frame, text="Processing Time (Hours)").grid(row=0, column=1, padx=5, pady=5) # Label for Processing Time
        ttk.Label(self.task_frame, text="Deadline (Hours)").grid(row=0, column=2, padx=5, pady=5) # Label for Deadline
        
        self.processing_time_entry = ttk.Entry(self.task_frame) # Entry for Processing Time
        self.processing_time_entry.grid(row=1, column=1, padx=5, pady=5) # Grid layout for Processing Time entry
        self.deadline_entry = ttk.Entry(self.task_frame) # Entry for Deadline
        self.deadline_entry.grid(row=1, column=2, padx=5, pady=5) # Grid layout for Deadline entry
        
        self.add_task_button = ttk.Button(self.task_frame, text="Add Task", command=self.add_task) # Button to add task
        self.add_task_button.grid(row=1, column=3, padx=5, pady=5) # Grid layout for Add Task button
        
        self.schedule_button_frame = ttk.Frame(self.root, padding="10") # Frame for schedule button
        self.schedule_button_frame.grid(row=2, column=0, sticky=(tk.W, tk.E)) # Grid layout for schedule button frame
        self.schedule_button_frame.configure(style="TFrame") # Configure style for schedule button frame

        self.schedule_button = ttk.Button(self.schedule_button_frame, text="Schedule Tasks", command=self.schedule_tasks) # Button to schedule tasks
        self.schedule_button.grid(row=0, column=0, padx=5, pady=5) # Grid layout for Schedule Tasks button
        
        self.result_frame = ttk.Frame(self.root, padding="10") # Frame to display the schedule
        self.result_frame.grid(row=3, column=0, sticky=(tk.W, tk.E)) # Grid layout for the frame
        
        self.tree = ttk.Treeview(self.result_frame, columns=("ID", "Processing Time", "Deadline", "Profit", "Vehicle"), show='headings') # Treeview to display the schedule
        self.tree.heading("ID", text="ID") # Heading for ID
        self.tree.heading("Processing Time", text="Processing Time (Hours)") # Heading for Processing Time
        self.tree.heading("Deadline", text="Deadline (Hours)") # Heading for Deadline
        self.tree.heading("Profit", text="Profit (₨)") # Heading for Profit
        self.tree.heading("Vehicle", text="Vehicle") # Heading for Vehicle
        
        self.tree.column("ID", width=50) # Column width for ID
        self.tree.column("Processing Time", width=150) # Column width for Processing Time
        self.tree.column("Deadline", width=150) # Column width for Deadline
        self.tree.column("Profit", width=100) # Column width for Profit
        self.tree.column("Vehicle", width=100) # Column width for Vehicle
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E)) # Grid layout for the treeview
        
    def add_task(self): # Add task to the list
        try: # Try to add task
            self.last_task_id += 1  # Increment the last task ID to generate a new unique ID
            task_id = self.last_task_id
            processing_time = int(self.processing_time_entry.get()) # Get processing time
            deadline = int(self.deadline_entry.get()) # Get deadline

            # Check if processing time or deadline is 0
            if processing_time == 0 or deadline == 0:
                messagebox.showerror("Invalid Input", "Processing time and deadline cannot be 0.")
                return  # Exit the method without adding the task

            # Check if deadline is less than processing time
            if deadline < processing_time:
                messagebox.showerror("Invalid Deadline", "Deadline cannot be less than processing time.")
                return  # Exit the method without adding the task

            new_task = Task(task_id, processing_time, deadline) # Create new task
            self.tasks.append(new_task) # Add task to the list
            
            self.tree.insert("", tk.END, values=(task_id, f"{processing_time} Hours", f"{deadline} Hours", new_task.get_profit_in_rupees(), "")) # Insert task into the treeview
            
            # Clear entries
            self.processing_time_entry.delete(0, tk.END) # Clear Processing Time entry
            self.deadline_entry.delete(0, tk.END) # Clear Deadline entry
        except ValueError: # Handle invalid input
            messagebox.showerror("Invalid Input", "Please enter valid integer values.") # Show error message
    
    def schedule_tasks(self): # Schedule tasks to vehicles
        num_vehicles = 30 # Number of vehicles
        schedule = schedule_delivery_tasks(self.tasks, num_vehicles) # Schedule tasks
        
        # Clear previous schedule
        for item in self.tree.get_children(): # Iterate over each item in the treeview
            self.tree.set(item, "Vehicle", "") # Clear vehicle information
        
        for task_id, vehicle in schedule: # Iterate over each task in the schedule
            for item in self.tree.get_children(): # Iterate over each item in the treeview
                if int(self.tree.item(item, "values")[0]) == task_id: # Check if the task ID matches
                    self.tree.set(item, "Vehicle", f"Vehicle {vehicle + 1}") # Set vehicle information

if __name__ == "__main__": # Run the application
    root = tk.Tk() # Create the root window
    app = DeliverySchedulerApp(root) # Create the application
    root.mainloop() # Run the application
