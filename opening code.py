import time
import sys

text1= "Welcome to the Arcade"
text2="Here are the instructions"
askingforname="Hi Player please enter your name"
instructions= ""

for char in text1:
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

for char in askingforname:
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

name=input("enter name here---> ")

beingnice = ("Nice to meet you ")
next_text = " LOADING...."

for char in beingnice:
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

for char in text2:
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

for char in instructions:
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

for char in "Lets Start!":
    sys.stdout.write(char)
    time.sleep(0.1)
sys.stdout.write('\n')

for char in next_text:
    sys.stdout.write(char)
    time.sleep(0.1)