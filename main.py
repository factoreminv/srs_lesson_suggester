import requests
import html5lib
import bs4
import numpy as np

def schedule(dept, course, sect, year, semester):

    url = f"https://stars.bilkent.edu.tr/syllabus/view/{dept}/{int(course)}/{int(year)}{int(semester)}?section={int(sect)}"
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.content, 'html5lib')

    lesson_plan = open(f"{dept}{course}-{sect}.txt", "w")
    for lesson in soup.find_all("b"):
        lesson_plan.write(str(lesson.parent.parent))

    lesson_plan.close()

    file = open(f"{dept}{course}-{sect}.txt", "r")

    line_mat = []
    final_mat = []

    for line in file:
        if "<td" == line[:3]:
            if "cl_ders_DY" in line:
                line_mat.append(line[line.index("text-align:center")+19: line.index("<", line.index("text-align:center")+22)])
            else:
                line_mat.append(0)

        if "</tr>" in line:
            final_mat.append(line_mat)
            line_mat = []

    return final_mat
def day_setter(mat):
    day_dict = {}
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    day_arr = np.array(mat).T
    day_mat = day_arr.tolist()
    day = 1

    for line in day_mat:
        day_dict[days[day]] = line
        day += 1

    return day_dict
def hour_finder(l_dict):
    fix_hours = {
        0: ("08:30", "09:20"), 1: ("09:30", "10:20"), 2: ("10:30", "11:20"), 3: ("11:30", "12:20"),
        4: ("12:30", "13:20"), 5: ("13:30", "14:20"), 6: ("14:30", "15:20"), 7: ("15:30", "16:20"),
        8: ("16:30", "17:20"), 9: ("17:30", "18:20"), 10: ("18:30", "19:20"), 11: ("19:30", "20:20"),
        12: ("20:30", "21:20"), 13: ("21:30", "22:20")
    }

    retlist = []

    for day in l_dict:
        for i in range(len(l_dict[day])):
            if l_dict[day][i] != "0":
                retlist.append((day, fix_hours[i][0], fix_hours[i][1], l_dict[day][i]))
    return retlist

day_schedule = day_setter(schedule("MAN","256","1","2022","1"))

print(hour_finder(day_schedule))
