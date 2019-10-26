import argparse
import random
import os
from playsound import playsound
import time
import csv

if __name__ == '__main__':
    randletter = chr(random.randint(65, 90))
    randint = str(random.randint(1, 10))
    pid = randletter + randint
    print(pid)

    audiofiles = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    print("info")
    
    if os.path.isfile('results.csv'):
        f = open('results.csv', 'a')
    else:
        f = open('results.csv', 'w')
    writer = csv.writer(f, delimiter=",")

    for i in range(len(audiofiles)):
        print("Playing sound")
        time.sleep(random.randint(1, 5))

        x = random.randint(0, len(audiofiles) - 1)
        playsound('audio/' + audiofiles[x] + '.mp3')

        rate = input("On a scale of 0 - 4 how clearly did you hear the sound? 0 - I did not hear anything, 4 - I heard it very clearly ")
        writer.writerow([pid, audiofiles[x], rate])
        audiofiles.pop(x)



