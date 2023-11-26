import pyautogui as pt
from time import sleep
import os

print("Working dir:", os.getcwd())
print("Files in here:", os.listdir("images"))

image_list = []

lesion1_directory = os.listdir('images/lesao1')
lesion2_directory = os.listdir('images/lesao2')

for file in lesion1_directory and lesion2_directory:
    if file.endswith('.png'):
        image_list.append(file)


# fazer função que ve o mob e digita oq ele está vendo
def lesion1():
    for image in image_list:
        position_lesion1 = pt.locateOnScreen(os.path.join('images\lesao1', image), confidence=0.5)
        if position_lesion1 is not None:
            return True
    return None


def lesion2():
    for image in image_list:
        position_lesion2 = pt.locateOnScreen(os.path.join('images\lesao2', image), confidence=0.5)
        if position_lesion2 is not None:
            return True
    return None


sleep(3)
duration = 1000
while duration != 0:
    detected_lesion1 = lesion1()
    detected_lesion2 = lesion2()
    if detected_lesion1 is not None:
        print(f'Lesão de grau 1 detectada:')
        break
    elif detected_lesion2 is not None:
        print(f'Lesão de grau 2 detectada:')
        break
else:
    print('Im not seein any images yet')

    duration -=1
