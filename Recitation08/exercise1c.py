def main():
    d={'CS101':['3004','Haynes','8:00 a.m.'], \
        'CS102':['4501','Alvarado','9:00 a.m.'], \
        'CS103':['6755','Rich','10:00 a.m.'], \
        'NT110':['1244','Burke','11:00 a.m.'], \
        'CM241':['1411','Lee','1:00 p.m.']}

    course_n = input('Enter course number: ')

    if course_n not in d:
        print('Course does not exist')
    else:
        print('Room number:', d[course_n][0])
        print('Instructor:', d[course_n][1])
        print('Meeting time:', d[course_n][2])



main()
