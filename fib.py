import tkinter as tk

def generate_fibonacci():
    n = int(entry.get())
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    output_label.config(text=f"Fibonacci Sequence: {fib_sequence}")

# Create the main window
root = tk.Tk()
root.title("Fibonacci Generator")

# Create widgets
label = tk.Label(root, text="Enter the number of Fibonacci numbers to generate:")
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate Fibonacci Sequence", command=generate_fibonacci)
generate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

# Run the Tkinter event loop
root.mainloop()
