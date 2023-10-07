from turtle import *
from tkinter import *
print("Welcome to our generative AI project.")

userGeneration = ''
# Setup the screen
sc = Screen()
sc.setup(width=0.75, height=0.75, startx=0, starty=0)
sc.bgcolor('white')



def mainFunction():
    global userGeneration
    hideturtle()
    write('Welcome to our Generative AI Project\n By: Blake Coppens And Zen Lambertus',
          align='center', font=('Times New Roman', 15, 'bold'))
    
    userGeneration = sc.textinput("Image Generator","Please Enter the item you would like to search for!")
    sc.clear()
    hideturtle()
    write(f'Searching for {userGeneration}... \n Please Wait', align='center',font=('Times New Roman', 15,'normal'))
    
    
## This is where we put your code, and we want to save the url to a 

# image = url

# Call the function to display the message
mainFunction()

# Start the turtle main loop
mainloop()
