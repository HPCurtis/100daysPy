import tkinter as tk

# Define constant variables
WIDTH_GUI = 100
HEIGHT_GUI = 100

import tkinter as tk

def miles_to_kilometers():
    try:
        miles = float(entry.get())
        kilometers = miles * 1.60934 
        result_label.config(text=f"{kilometers:.2f} Kilometers")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Generate instance of Tk class.
window = tk.Tk()

# Set the title and minimum size of the window
window.title("Miles to Kilometers")
window.minsize(width=300, height=100)

# Create and place the label for "Miles"
L1 = tk.Label(window, text="Miles:")
L1.pack(side="left", padx=(20, 5))

# Create and place the entry widget for user input
entry = tk.Entry(window, bd=5)
entry.pack(side="left", padx=5)

# Create and place the button to trigger the conversion
B = tk.Button(window, text="Calculate", command=miles_to_kilometers)
B.pack(side="left", padx=(5, 20))

# Create and place the label to display the result
result_label = tk.Label(window, text="")
result_label.pack(side="left", padx=(5, 20))

# Create a loop to keep the GUI on screen.
window.mainloop()
