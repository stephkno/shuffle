#!/usr/local/bin/python3
#
# shuffle
#
# shuffles all audio files in working directory
# supporting macOS only
#

import os
import random
import atexit

cd = "."
files = [file for file in os.listdir(cd) if os.path.isfile(file)]
random.shuffle(files)
print("Shuffling {} songs in {}".format(len(files), os.getcwd()))

audio_formats = ["m4a", "mp3", "wav", "aac", "aifc"]

total = len(files)
current = 1

def exit():
    os.system('killall afplay > /dev/null')

atexit.register(exit)
print('Press return to skip track')

for f in files:
    print("Playing file [{}/{}]: ".format(current, total) + f)
    os.system('afplay \"' + f + '\" &') if f.split(".")[-1] in audio_formats else 0
    # press return to skip track
    input()

    current+=1
    os.system('killall afplay')
