# to pretend to be a computer and have a "conversation"# importing required packagesimport timeimport sys# introducing the first texttext1 = "Hello I am Mac OS"# instead of using print we write the text1 so that it does not turn into a string.# Print turns it into a string but by using write we can play with the internal charactersfor char in text1:    sys.stdout.write(char)    time.sleep(0.2)# print prints in different lines but write does not so we need to add it using below linesys.stdout.write('\n')# second text which is followed by inputtext2 = "what is your name? "for char in text2:    sys.stdout.write(char)    time.sleep(0.2)sys.stdout.write('\n')# input str namename_variable = input("Enter Name Here - ")#Next lines that are to be displayedtext = ("Nice to meet you ")next_text = " LOADING...."#displying a responsefor char in text:    sys.stdout.write(char)    time.sleep(0.2)for char in name_variable:    sys.stdout.write(char)    time.sleep(0.2)time.sleep(1.0)sys.stdout.write('\n')# game here is turtlefor char in "Let's play a game":    sys.stdout.write(char)    time.sleep(0.2)time.sleep(1.0)sys.stdout.write('\n')#taking input for the gamefor char in "Enter a number, preferably between 1 to 10--> ":    sys.stdout.write(char)    time.sleep(0.2)time.sleep(1.0)n=int(input( ))# loading textfor char in next_text:    sys.stdout.write(char)    time.sleep(0.2)time.sleep(1.0)import turtleturtle.bgcolor("black")turtle.pensize(2)turtle.speed(0)for i in range(n):    for colours in ["red", "magenta", "blue", "cyan",  "white", "green" ]:     turtle.color(colours)     turtle.circle(50)     turtle.right(20)turtle.hideturtle()turtle.done()