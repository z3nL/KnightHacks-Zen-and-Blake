# Created for KnightHacks2023 By Blake Coppens And Zen Lambertus
# Description: A project taking use of OpenAI in order to generate images
# From a custom made user interface. 
# Potential Changes: Looking into using Semantic Kernel or MondoDB in order
# To search larger areas 
from turtle import *
import turtle
from tkinter import *
import os
import openai
from dotenv import load_dotenv
import requests
from io import BytesIO
from PIL import Image, ImageTk
#listing all the imports

# Global variables referenced later
userGeneration = ''
image_url = ''
hasRun = True
button1=None
button2=None



def get_image_from_url(url):  #    Fetches image from the provided URL and returns it as an ImageTk.PhotoImage object
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    
    # Convert PIL image to a format that turtle can use
    image_tk = ImageTk.PhotoImage(image)
    return image_tk


load_dotenv() #loads the OpenAI key
openai.api_key = os.environ.get("OPEN_AP_I_KEY")

def imageSearch(userPrompt): #using our OpenAI key to create a url, with a parameter that defines what image is generated
    global image_url
    response = openai.Image.create(
    prompt=userPrompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url'] # Stores the imageURL, and allows us to save it.
    print(image_url)

# Setup the screen
sc = Screen()
sc.setup(width=0.75, height=0.75, startx=0, starty=0)
sc.bgcolor('white')

#prints the screen, using the URL generated as the canvas
def printToScreen():
    global hasRun,button1,button2
    image = get_image_from_url(image_url)
    sc.addshape("custom", turtle.Shape("image", image))
    t = turtle.Turtle()
    t.shape("custom")
    if hasRun == True: #A code to pack the button only once, so even if the function is called upon it doesnt add more buttons
        canvas = sc.getcanvas()
        button1 = Button(canvas.master, text="Regenerate", command=regen)
        button1.pack()
        button2 = Button(canvas.master, text="Search", command=searchIOT)
        button2.pack()
        hasRun=False
    turtle.mainloop()
    
def regen(): # Regen image function
    global userGeneration
    imageSearch(userGeneration)
    printToScreen()
    

def searchIOT(): #Clears the image, originally planned to reference internet
    button1.pack_forget()
    button2.pack_forget()
    turtle.clearscreen()
    
    
def mainFunction(): #main fuction, what is run when the program starts
    global userGeneration, image_url, sc, turtle
    hideturtle()
    write('Welcome to our Generative AI Project\n By: Blake Coppens And Zen Lambertus',
          align='center', font=('Times New Roman', 15, 'bold')) #credits
    
    userGeneration = sc.textinput("Image Generator","Please Enter the item you would like to search for!")
    print(userGeneration)
    with open('KnightHacks-Zen-and-Blake\Searches.txt', 'a') as file:
        file.write('\n' + userGeneration)
    sc.clear()
    hideturtle()
    write(f'Searching for {userGeneration}... \n Please Wait', align='center',font=('Times New Roman', 15,'normal'))
    imageSearch(userGeneration)
    printToScreen()


mainFunction()
