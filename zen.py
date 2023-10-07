import os
import openai
from dotenv import load_dotenv

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

userPrompt = input('What clothing item would you like to generate:\n')
#imageSearch(userPrompt)

check = 0
while check != '4':
    if check == '1':
        imageSearch(userPrompt)
    elif check == '2':
        userPrompt = input('Enter new prompt below:\n')
        imageSearch(userPrompt)
    elif check == '3':
        print('Ok we go')
        break
    check = input('Select Regenerate (1), Change Prompt (2), Proceed (3), or Exit (4): ')
    if check == '4':
        SystemExit