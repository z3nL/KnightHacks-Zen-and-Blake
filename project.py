from turtle import *
import turtle
from tkinter import *
import os
import openai
from dotenv import load_dotenv
import requests
from io import BytesIO
from PIL import Image, ImageTk

def get_image_from_url(url):
    """Fetches image from the provided URL and returns it as an ImageTk.PhotoImage object."""
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    
    # Convert PIL image to a format that turtle can use
    image_tk = ImageTk.PhotoImage(image)
    
    return image_tk



load_dotenv()
openai.api_key = os.environ.get("OPEN_AP_I_KEY")

def imageSearch(userPrompt):
    global image_url
    response = openai.Image.create(
    prompt=userPrompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    
print("Welcome to our generative AI project.")

userGeneration = ''
image_url = ''
hasRun = True
button1=None
button2=None
# Setup the screen
sc = Screen()
sc.setup(width=0.75, height=0.75, startx=0, starty=0)
sc.bgcolor('white')

def printToScreen():
    global hasRun,button1,button2
    image = get_image_from_url(image_url)
    sc.addshape("custom", turtle.Shape("image", image))
    t = turtle.Turtle()
    t.shape("custom")
    if hasRun == True:
        canvas = sc.getcanvas()
        button1 = Button(canvas.master, text="Regenerate", command=regen)
        button1.pack()
        button2 = Button(canvas.master, text="Search", command=searchIOT)
        button2.pack()
        hasRun=False
    turtle.mainloop()
def regen():
    global userGeneration
    imageSearch(userGeneration)
    printToScreen()
    

def searchIOT():
    button1.pack_forget()
    button2.pack_forget()
    turtle.clearscreen()
    
    
def mainFunction():
    global userGeneration, image_url, sc, turtle
    hideturtle()
    write('Welcome to our Generative AI Project\n By: Blake Coppens And Zen Lambertus',
          align='center', font=('Times New Roman', 15, 'bold'))
    
    userGeneration = sc.textinput("Image Generator","Please Enter the item you would like to search for!")
    sc.clear()
    hideturtle()
    write(f'Searching for {userGeneration}... \n Please Wait', align='center',font=('Times New Roman', 15,'normal'))
    imageSearch(userGeneration)
    printToScreen()


mainFunction()
