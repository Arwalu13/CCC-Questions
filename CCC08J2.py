buttonPress = ''
playlist = ['A', 'B', 'C', 'D', 'E']


while buttonPress != 4:
    buttonPress = int(input())
    numOfPresses = int(input())

    if buttonPress == 1:
        for i in range(0, numOfPresses):
            firstSong = playlist[0]
            for i in range(0, 4):
                playlist[i] = playlist[i + 1]
            playlist[-1] = firstSong

    if buttonPress == 2:
        for i in range(0, numOfPresses):
            lastSong = playlist[-1]
            for i in range(3, -1, -1):
                playlist[i + 1] = playlist[i]
            playlist[0] = lastSong

    if buttonPress == 3:
        for i in range(0, numOfPresses):
            playlist[0], playlist[1] = playlist[1], playlist[0]

for i in range(5):
    print(playlist[i], end = ' ')
        
print('')