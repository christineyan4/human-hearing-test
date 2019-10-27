import argparse
import random
import os
from playsound import playsound
import time
import csv

def prescreen(pid, pswriter):
    age = input("How old are you?\n")
    issues = input("Have you ever had any hearing-related issues (ex: hearing loss, ear infections)? Y/N\n")
    pswriter.writerow([pid, age, issues])

def hearing_test(pid, audiofiles, htwriter):
    for i in range(len(audiofiles)):
        print("Playing sound")
        wait = time.sleep(random.randint(1, 5))

        x = random.randint(0, len(audiofiles) - 1)
        playsound('audio/' + audiofiles[x] + 'Hz.mp3')
        time.sleep(5 - wait)

        rate = input("On a scale of 0 - 4 how clearly did you hear the sound? 0 - I did not hear anything, 4 - I heard it very clearly\n")
        htwriter.writerow([pid, audiofiles[x], rate])
        audiofiles.pop(x)

if __name__ == '__main__':
    randletter = chr(random.randint(65, 90))
    randint = str(random.randint(1, 10))
    pid = randletter + randint
    print(pid)

    audiofiles = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    print("Welcome to our study. We will be playing different frequencies at varying volumes. There will be a prescreen, followed by a test tone before beginning the hearing test. Please do not adjust the volume.")

    if os.path.isfile('prescreen.csv'):
        f = open('prescreen.csv', 'a')
    else:
        f = open('prescreen.csv', 'w')
    pswriter = csv.writer(f, delimiter=",")
    prescreen(pid, pswriter)

    print("Playing test tone...\n")
    # playsound("test.mp3")
    input("Press enter to begin.\n")

    if os.path.isfile('results.csv'):
        f = open('results.csv', 'a')
    else:
        f = open('results.csv', 'w')
    htwriter = csv.writer(f, delimiter=",")
    hearing_test(pid, audiofiles, htwriter)
