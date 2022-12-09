import tkinter as tk

department_list = []

def save_department():
    entry = str(c1.get()).upper()
    department_list.append(entry)
    text_box.insert("1.0",entry+"\n")

def class_look():
    master.destroy()
    return department_list

master = tk.Tk()
tk.Label(master,
         text="Department").grid(row=0)

c1 = tk.Entry(master)

text_box = tk.Text()
text_box.grid(row=1,column=1)

c1.grid(row=0, column=1)

tk.Button(master,
          text='Add', command=save_department).grid(row=2,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
tk.Button(master,
          text='Display Classes', command=class_look).grid(row=2,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()
