import tkinter as tk
from Querry import T_file_search
from datetime import datetime

department_list = []

def save_department():
    entry = str(c1.get()).upper()
    c1.delete("0", tk.END)
    department_list.append(entry)
    text_box.insert("1.0",entry+"\n")

def Time_class_look():
    c1.delete("0", tk.END)
    text_box.delete("1.0", tk.END)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%A")

    #current_time = "12:20"
    #current_day = "Wednesday"

    k = 1

    for department in department_list:
        classes = T_file_search(department+".txt", current_time[:5], current_day)

        text_box.insert(str(k)+".0", department+"\n")
        text_box.insert(str(k+1) + ".0", "\n")

        k += 2

        for i in range(len(classes)):
            text_box.insert(str(k+i+1)+".0", classes[i][0]+"   "+classes[i][1]+classes[i][2]+"-"+classes[i][3]+" "+classes[i][5]+" "+classes[i][4]+"\n")
            t = i
        k += t+1

        text_box.insert(str(k + 1) + ".0", "\n")
        text_box.insert(str(k + 1) + ".0", "\n")
        k += 2
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
          text='Display Classes', command=Time_class_look).grid(row=2,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()
