import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=2000, height=2000, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
T = tk.Text(root, height=1000, width=1000)
# T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

canvas.create_circle(50, 70, 20, fill="#BBB", outline="#DDD")

root.wm_title("Circles and Arcs")
root.mainloop()
