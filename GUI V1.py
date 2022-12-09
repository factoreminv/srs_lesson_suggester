import tkinter as tk
from main import hour_finder, day_setter, schedule

def show_entry_fields():
    try:
        lis = hour_finder(day_setter(schedule(c1.get(), c2.get(), c3.get(), "2022", "1")))
        i = 1
        text_box.delete("1.0", tk.END)
        for tup in lis:
            #print(tup[0],tup[1]+" - "+tup[2])
            text_box.insert(str(i)+".0",tup[0]+" "+tup[1]+" - "+tup[2]+" "+tup[3]+" "+tup[4]+"\n")
            i += 1
    except:
        text_box.delete("1.0", tk.END)
        text_box.insert("1.0","CLASS NOT FOUND\n")


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

text_box = tk.Text()
text_box.grid(row=3,column=1)

c1.grid(row=0, column=1)
c2.grid(row=1, column=1)
c3.grid(row=2, column=1)

tk.Button(master,
          text='List', command=show_entry_fields).grid(row=4,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()
