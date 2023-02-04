import tkinter as tk

def show_table(n):
    result.config(text="")
    for i in range(1, 13):
        result.config(text=result.cget("text") + f"{n} x {i} = {n*i}\n")

root = tk.Tk()
root.title("Multiplication Table")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack()

button = tk.Button(root, text="Show Table", font=("Arial", 20), command=lambda: show_table(int(entry.get())))
button.pack()

result = tk.Label(root, font=("Arial", 20))
result.pack()

root.mainloop()
