import tkinter as tk
from main import hour_finder, day_setter, schedule

def show_entry_fields():
    lis = hour_finder(day_setter(schedule(c1.get(), c2.get(), c3.get(), "2022", "1")))
    for tup in lis:
        print(tup[0],tup[1]+" - "+tup[2])

master = tk.Tk()
tk.Label(master,
         text="Department").grid(row=0)
tk.Label(master,
         text="Course").grid(row=1)
tk.Label(master,
         text="Section").grid(row=2)

c1 = tk.Entry(master)
c2 = tk.Entry(master)
c3 = tk.Entry(master)

c1.grid(row=0, column=1)
c2.grid(row=1, column=1)
c3.grid(row=2, column=1)

tk.Button(master,
          text='List', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()
