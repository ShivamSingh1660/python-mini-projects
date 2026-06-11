import tkinter as tk

root = tk.Tk()

def hello():
    print("Hello Shivam!")

btn = tk.Button(root, text="Click Me", command=hello)
btn.pack()

root.mainloop()