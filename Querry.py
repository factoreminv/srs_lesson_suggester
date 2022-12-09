from main import hour_finder, day_setter, schedule
from datetime import datetime

def querry(dept):
    class_list =[]
    for n in range(101, 499):
        try:
            lis = hour_finder(day_setter(schedule(dept, n, "1", "2022", "1")))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_day = now.strftime("%A")

            for element in lis[0::2]:
                if element[0] == current_day and element[1] > "13:20":
                    class_list.append(tuple([dept]) + tuple([str(n)]) + tuple(lis))
        except:
            None
    return class_list


print(querry("MATH"))
