import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
image_path = input("Your image path:")

allowed = ['jpg', 'png', 'webp', 'jpeg', 'gif']

isValidFormat = False
isValidStructure = False
format = ""

if "." in image_path:
    isValidStructure = True
    format = image_path.split(".")[1]

if isValidStructure == False:
    print("Image path is not structured correctly!")

else:
    for item in allowed:
        if item == format:
            isValidFormat = True
            break

    if isValidFormat == False:
        print("Image has to be in .jpg/.png/.webp/.jpeg/.gif format!")

    else:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(image_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )

        if response.status_code == requests.codes.ok:
            with open(f'{image_path.split(".")[0]}-no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)