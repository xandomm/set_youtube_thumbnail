from PIL import Image, ImageDraw, ImageFont
from numpy import interp
import time

def buildClock():
    # getting time
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    dayTime = time.strftime("%p")
    
    # getting hands angles 
    mAngle = 360/60 * int(minutes)
    hAngle = 360/12 * int(hours) + interp(mAngle, [0, 360], [0, 30])
    
    # Rotating Pointers
    # hour hand
    hours_handImg = Image.open('set_image/images/clock/hourPointer.png')
    hours_hand_rotate = hours_handImg.rotate(-hAngle)
    # hours_hand_rotate.save('images/hourPointerRotate.png')

    # minutes hand 
    minutes_handImg = Image.open('set_image/images/clock/minutesPointer.png')
    minutes_hand_rotate = minutes_handImg.rotate(-mAngle)
    # minutes_hand_rotate.save('images/minutesPointerRotate.png')

    # building final image
    finalImage = Image.open("set_image/images/clock/clockBg.png")
    finalImage.paste(minutes_hand_rotate, (200,200), minutes_hand_rotate)
    finalImage.paste(hours_hand_rotate, (200,200), hours_hand_rotate)

    # finalImage.show()

    # generate text
    time_text = hours + ":" + minutes + ":" + seconds + dayTime
    drawTxt = ImageDraw.Draw(finalImage) 

    # specified font size
    font = ImageFont.truetype('set_image/VisbyRoundCF-ExtraBold.otf', 150) 

    
    
    drawTxt.text((250, 1050), time_text, font=font, align='center')
    # finalImage.show()
    finalImage.save('set_image/images/clock/final_clock.png')


# clock()