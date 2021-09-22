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

    user_input = input('Course Number:\n> ')

    if user_input not in room_number.keys():
        print('The course is not in the list')
    else:
        print('Room number:', room_number[user_input])
        print('Instructor:', instructor[user_input])
        print('Meeting Time:', meeting_time[user_input])

    
    
main()
