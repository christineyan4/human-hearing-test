import argparse
import random
import os
from playsound import playsound
import time
import csv

def generate_pid():
    randomletter = chr(random.randint(65, 90))
    randomint = str(random.randint(1, 10))
    pid = randomletter + randomint
    return pid

def prescreen(pid, pswriter):
    print("Welcome to our study. We will be playing different freqs at varying volumes. There will be a prescreen, followed by a test tone before beginning the hearing test. Please do not adjust the volume.")

    age = input("How old are you?\n")
    issues = input("Have you ever had any hearing-related issues (ex: hearing loss, ear infections)? Y/N\n")

    print("Playing test tone...\n")
    playsound("audio/test.mp3")
    input("Press enter to begin.\n")

    pswriter.writerow([pid, age, issues])

def hearing_test(pid, freqs, htwriter):
    for i in range(len(freqs)):
        print("Playing sound...\n")
        wait = random.randint(1, 5)
        time.sleep(wait)

        x = random.randint(0, len(freqs) - 1)
        playsound('audio/' + freqs[x] + 'Hz.mp3')
        time.sleep(5 - wait)

        rate = input("On a scale of 0 - 4 how clearly did you hear the sound? 0 - I did not hear anything, 4 - I heard it very clearly\n")
        htwriter.writerow([pid, freqs[x], rate])
        freqs.pop(x)

if __name__ == '__main__':
    pid = generate_pid()
    freqs = ['1000', '100', '120', '14000', '140', '160', '18000', '180', '20000', '200', '20', '3000', '30', '400', '40', '5000', '50', '600', '60', '7000', '70', '800', '80', '9000']

    if os.path.isfile('prescreen.csv'):
        f = open('prescreen.csv', 'a')
    else:
        f = open('prescreen.csv', 'w')

    pswriter = csv.writer(f, delimiter=",")
    prescreen(pid, pswriter)

    if os.path.isfile('results.csv'):
        f = open('results.csv', 'a')
    else:
        f = open('results.csv', 'w')

    htwriter = csv.writer(f, delimiter=",")
    hearing_test(pid, freqs, htwriter)
