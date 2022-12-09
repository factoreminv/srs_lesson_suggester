# coding=UTF-8

from main import hour_finder, day_setter, schedule
from datetime import datetime

def querry(dept):
    class_list =[]
    for n in range(101, 499):
        for sect in range(1,20):
            try:
                lis = hour_finder(day_setter(schedule(dept, n, sect, "2022", "1")))
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_day = now.strftime("%A")

                for element in lis[0::2]:
                    if element[0] == current_day and element[1] > "13:20":
                        class_list.append(tuple([dept]) + tuple([str(n)]) +tuple([sect]) + tuple(lis))
                        print(tuple([dept]) + tuple([str(n)]) +tuple([sect]) + tuple(lis))
            except:
                None
    return class_list

def create_querry_file(dept):
    file = open(dept+".txt","w",encoding="utf-8")
    for n in range(101, 499):
        for sect in range(1,20):
            try:
                lis = hour_finder(day_setter(schedule(dept, n, sect, "2022", "1")))
                file.write(str(tuple([dept]) + tuple([str(n)]) + tuple([str(sect)]) + tuple(lis))+"\n")
                print(str(tuple([dept]) + tuple([str(n)]) + tuple([str(sect)]) + tuple(lis)))
            except:
                break
    file.close()

def file_search(filename, instructor):
    instructor.encode(encoding="UTF-8", errors="strict")
    retlist = []
    file = open(filename, "r", encoding="utf-8")
    for line in file:
        line = line.strip().replace("(","").replace(")","").replace("'","").replace("'","").split(",")
        try:
            if instructor in line[7]:
                retlist.append(line[:3])
        except:
            None
    return retlist


#querry("PHYS")
#create_querry_file("EEE")
print(file_search("MATH.txt", "Orhan Arıkan"))
