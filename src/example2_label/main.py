import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()

    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()

    # When you pack a widget into a window, Tkinter sizes the window as small as it can
    # be while still fully encompassing the widget. This is called "packing" the widget.

    window.mainloop()
