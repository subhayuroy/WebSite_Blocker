import requests
from io import BytesIO
from PIL import Image

link = input("Enter the link: ")
# r = requests.get("https://wallpapercave.com/wp/BcXToWf.jpg")
r = requests.get(link)
print("Status code:", r.status_code)
image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")