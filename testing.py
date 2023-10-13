'''
Hi! This is a miscellaneous file we utilized to test usage with various API's and statements
as we advanced in our project. While relevant to our very little progress, this file has no actual relation
to project.py
'''

# various imports
from bs4 import BeautifulSoup

import os
import openai
from dotenv import load_dotenv
import requests
import cv2
import numpy as np
import PIL
from PIL import Image
from io import BytesIO

# first time working with a .env file! very interesting to see how such a small step can go a long way in project security
load_dotenv()
openai.api_key = os.environ.get("OPEN_AP_I_KEY")

# function taken from OpenAI's API help website
def imageSearch(userPrompt):
    response = openai.Image.create(
    prompt=userPrompt,
    n=1,
    size="1024x1024"
    )
    image_url1 = response['data'][0]['url']
    print(image_url1)
    return(image_url1)

# Asks user image they would want generated
userPrompt = input('What clothing item would you like to generate:\n')
image_url1 = imageSearch(userPrompt)

# Generates image and checks for user's response to current image displayed
check = 0
while check != '4':
    if check == '1':
        image_url1 = imageSearch(userPrompt)
    elif check == '2':
        userPrompt = input('Enter new prompt below:\n')
        image_url1 = imageSearch(userPrompt)
    elif check == '3':
        print('Ok we go')
        break
    check = input('Select Regenerate (1), Change Prompt (2), Proceed (3), or Exit (4): ')
    if check == '4':
        SystemExit

'''
response = requests.get(image_url)
image_data = response.content 
generated_image = cv2.imdecode(np.frombuffer(image_data, np.uint8), -1)

site_url= 'https://us.shein.com/'
response2 = requests.get(site_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find product titles and image URLs
product_titles = [item.text for item in soup.find_all('h2', class_='product-title')]
print(product_titles)
image_urls = [item['src'] for item in soup.find_all('img', class_='product-image')]
print(image_urls)
'''
image_url2 = input("Give second image's url:\n")
##############################
# Function to get image resolution from URL
def get_image_resolution(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    return width, height

# Get resolutions of the two images
resolution1 = get_image_resolution(image_url1)
resolution2 = get_image_resolution(image_url2)

# Compare resolutions
if resolution1 > resolution2:
    larger_image_url = image_url1
    smaller_image_url = image_url2
    larger_resolution = resolution1
    smaller_resolution = resolution2
else:
    larger_image_url = image_url2
    smaller_image_url = image_url1
    larger_resolution = resolution2
    smaller_resolution = resolution1

# Resize the larger image to match the resolution of the smaller image
larger_image = Image.open(BytesIO(requests.get(larger_image_url).content))
larger_image = larger_image.resize(smaller_resolution, PIL.Image.Resampling.LANCZOS)

# Save the resized image
larger_image.save("resized_image.jpg")

print("Resized image saved as resized_image.jpg")
##############################

response = requests.get(smaller_image_url)
smaller_image_data = response.content 
smaller_image = cv2.imdecode(np.frombuffer(smaller_image_data, np.uint8), -1)


#response2 = requests.get(image_url2)
#sourced_image_data = response2.content 
#sourced_image = cv2.imdecode(np.frombuffer(sourced_image_data, np.uint8), -1)

# load the input images
img2 = cv2.imread("resized_image.jpg")

# convert the images to grayscale
img1 = cv2.cvtColor(smaller_image, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()