
Mov = []

while True:
    print('Movie No' + str(len(Mov)+1) + ' or press Enter to stop the adding list')
    Movie = input()
    if Movie == '':
        break
    Mov = Mov +[Movie]
if len(Mov) != 0:
    print('The Movie Lists are ')
    for i in range(len(Mov)):
        print(Mov[i])
