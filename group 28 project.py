from microbit import *
from random import *
import music


images = (Image.HAPPY, Image.SAD, Image.GHOST, Image.SKULL, Image.DUCK, Image.UMBRELLA,Image.GIRAFFE,Image.RABBIT,Image.HEART, Image.ANGRY, Image.STICKFIGURE)
while True:
    sleep(20)
    x = randint(0, 4)
    y = randint(0, 4)
    brightness = randint(0, 9)
    display.set_pixel(x, y, brightness)
    if pin2.read_digital() == False :
        if button_a.is_pressed():
            display.show(choice(images))
            sleep(500)
        elif button_b.is_pressed():
            display.scroll("Group 28's project!", delay = 80)
    elif pin2.read_digital() == True :
        display.show(Image.STICKFIGURE, delay = 10)
        music.play("C4:100")
