import os
from PIL import Image

for direction in ('right', 'left'):
    for i in range(1, 7):
        image_path = f'images/enemies/Crab/{direction}/{i}.png'
        folder_path = f'images/enemies/TermenatorCrab/{direction}/{i}.png'

        img = Image.open(image_path)
        # получаем ширину и высоту
        width, height = img.size
        new_image = img.resize((width * 48, height * 48))
        file_path = os.path.join(folder_path)
        new_image.save(file_path)
