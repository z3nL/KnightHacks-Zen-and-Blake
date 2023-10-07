import os
import openai
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np

load_dotenv()
openai.api_key = os.environ.get("OPEN_AP_I_KEY")

def imageSearch(userPrompt):
    response = openai.Image.create(
    prompt=userPrompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    return(image_url)

userPrompt = input('What clothing item would you like to generate:\n')
image_url = imageSearch(userPrompt)

check = 0
while check != '4':
    if check == '1':
        image_url = imageSearch(userPrompt)
    elif check == '2':
        userPrompt = input('Enter new prompt below:\n')
        image_url = imageSearch(userPrompt)
    elif check == '3':
        print('Ok we go')
        break
    check = input('Select Regenerate (1), Change Prompt (2), Proceed (3), or Exit (4): ')
    if check == '4':
        SystemExit

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

# Store the extracted data or continue with feature extraction and comparison.
