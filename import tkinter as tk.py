import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Create a tkinter window
window = tk.Tk()
window.title("Garden Planner")

# Create a canvas for garden layout
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Function to add a plant to the garden
def add_plant():
    plant_name = plant_entry.get()
    x_pos = int(x_entry.get())
    y_pos = int(y_entry.get())
    
    # Create a data frame to store plant data
    garden_data = pd.DataFrame({'Plant Name': [plant_name], 'X Position': [x_pos], 'Y Position': [y_pos]})
    
    # Append new plant data to the existing or new CSV file
    with open('garden_data.csv', 'a') as f:
        garden_data.to_csv(f, header=f.tell()==0, index=False)
    
    # Draw a point on the canvas to represent the plant
    canvas.create_oval(x_pos-5, y_pos-5, x_pos+5, y_pos+5, fill='green', outline='green')
    
    # Clear input fields
    plant_entry.delete(0, tk.END)
    x_entry.delete(0, tk.END)
    y_entry.delete(0, tk.END)

# Function to visualize the garden
def visualize_garden():
    # Read plant data from the CSV file
    garden_data = pd.read_csv('garden_data.csv')
    
    # Create a scatter plot of plant positions
    plt.scatter(garden_data['X Position'], garden_data['Y Position'], marker='o', c='green')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Garden Layout')
    plt.grid(True)
    plt.show()

# Create labels and entry fields for adding plants
plant_label = tk.Label(window, text="Plant Name:")
plant_label.pack()
plant_entry = tk.Entry(window)
plant_entry.pack()

x_label = tk.Label(window, text="X Position:")
x_label.pack()
x_entry = tk.Entry(window)
x_entry.pack()

y_label = tk.Label(window, text="Y Position:")
y_label.pack()
y_entry = tk.Entry(window)
y_entry.pack()

add_button = tk.Button(window, text="Add Plant", command=add_plant)
add_button.pack()

visualize_button = tk.Button(window, text="Visualize Garden", command=visualize_garden)
visualize_button.pack()

# Start the tkinter main loop
window.mainloop()