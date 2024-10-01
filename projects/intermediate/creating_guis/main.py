# Import packages
import tkinter

# Define constant variables
WIDTH_GUI = 300
HEIGHT_GUI = 300

# Generate isntance to Tk class.
window = tkinter.Tk()

window.title("First GUI")
window.minsize(width = WIDTH_GUI, height = HEIGHT_GUI)

# USe the label method
label = tkinter.Label(text = 'Label', font = ("Arial", 24, "bold"))
label.pack(side="bottom")

# Create a loop to keep the GUI on screen.
window.mainloop()