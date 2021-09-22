def main():
    # empty dict
    capitals = {}
    
    f = open('chinese-provincial-capitals.txt', 'r')

    #read first line (header) (do not do anything with it)
    f.readline()
    
    for s in f:
        #remove '\n' at the end
        s = s.rstrip()

        #item separator is comma ','
        list = s.split(',')

        #add entry to the dict
        capitals[list[0]] = list[1]

    correct = incorrect = 0
    
    keep_playing = True
    
    while keep_playing:
        user_input = input('Continue? (y or n)')

        if user_input == 'n':
            keep_playing = False
        else:
            #random question (temporarily removed from dict)
            question = capitals.popitem()
            #put it back in the dict
            capitals[question[0]] = question[1]

            print('What is the capital of ' + question[0] + '?')
            answer = input('Answer: ')

            if answer == question[1]:
                correct += 1
                print('Correct')
            else:
                incorrect += 1
                print('Incorrect')

            print('Total of correct answers:', correct)
            print('Total of incorrect answers:', incorrect)

main()
