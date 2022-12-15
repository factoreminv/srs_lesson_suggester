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
    for n in range(101, 700):
        for sect in range(1,100):
            try:
                lis = hour_finder(day_setter(schedule(dept, n, sect, "2022", "1")))
                file.write(str(tuple([dept]) + tuple([str(n)]) + tuple([str(sect)]) + tuple(lis))+"\n")
                print(str(tuple([dept]) + tuple([str(n)]) + tuple([str(sect)]) + tuple(lis)))
            except:
                break
    file.close()

def I_file_search(filename, instructor, sel="T"):
    instructor.encode(encoding="UTF-8", errors="strict")
    retlist = []
    file = open(filename, "r", encoding="utf-8")
    for line in file:
        line = line.strip().replace("(","").replace(")","").replace("'","").replace("'","").split(",")
        try:
            if instructor in line[7]:
                retlist.append(line[:3]+line[6:8])
        except:
            None
    return retlist

def T_file_search(filename, time, day):

    retlist = []
    file = open(filename, "r", encoding="utf-8")
    for line in file:
        line = line.strip().replace(", ",",").replace("(","").replace(")","").replace("'","").replace("'","").split(",")
        try:
            if day in line[3] and time < line[4]:
                retlist.append([line[4]] + line[:3] + line[6:9])
            if day in line[15] and time < line[16]:
                retlist.append([line[16]] + line[:3] + line[6:9])
        except:
            None


    #SORTING FOR ASCENDING TIME

    for step in range(len(retlist)):
        min_idx = step

        for i in range(step + 1, len(retlist)):

            if retlist[i][0] < retlist[min_idx][0]:
                min_idx = i

        # put min at the correct position
        (retlist[step], retlist[min_idx]) = (retlist[min_idx], retlist[step])

    return retlist


def main():
    pass

if __name__ == "__main__":
    main()
    # querry("PHYS")
    create_querry_file("MATH")
    # print(T_file_search("PHYS.txt", "13:20", "Tuesday"))
