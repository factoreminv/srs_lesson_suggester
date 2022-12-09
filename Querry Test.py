from main import hour_finder, day_setter, schedule

for n in range(101,499):
    try:
        print(hour_finder(day_setter(schedule("MATH", n, "1", "2022", "1"))))
    except:
        print("No Such Course")