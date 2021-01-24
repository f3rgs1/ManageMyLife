import tkinter as tk

# sets root window object
window = tk.Tk()
# sets title
window.title("Manage My Life")
# sets default size of window
window.geometry("700x350")

# adds a widget to the GUI
greetingwidget = tk.Label(text="Greetings!")
greetingwidget.pack()
# blocks program, any code after here will not run. Consider using update().
window.mainloop()
