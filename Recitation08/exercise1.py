def main():
    room_number = {
        "CS101":"3004",
        "CS102":"4501",
        "CS103":"6755",
        "NT110":"1244",
        "CM241":"1411"}

    instructor = {
        "CS101":"Haynes",
        "CS102":"Alvarado",
        "CS103":"Rich",
        "NT110":"Burke",
        "CM241":"Lee"}

    meeting_time = {
        "CS101":"8:00 a.m.",
        "CS102":"9:00 a.m.",
        "CS103":"10:00 a.m.",
        "NT110":"11:00 a.m.",
        "CM241":"1:00 p.m."}
    
    course_list = room_number.keys()

    course_number = input('Course Number?\n> ')

    if course_number not in course_list:
        print('This course is not in the list')
    else:
        print('Room Number:', room_number[course_number])
        print('Instructor:', instructor[course_number])
        print('Meeting Time:', meeting_time[course_number])

        
main()
