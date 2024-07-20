import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

app = tk.Tk()
app.title("Simple Tkinter App")

label = tk.Label(app, text="Welcome!")
label.pack()

button = tk.Button(app, text="Click Me", command=say_hello)
button.pack()

app.mainloop()

