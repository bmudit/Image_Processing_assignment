#importing necessary libraries
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
%matplotlib inline


# FIRST SET


#importing first background(bag1) and threat image (t1)
bag1 = Image.open('background_images/bg1.jpg')
t1 = Image.open('threat_images/t1.jpg')

#croping and rotating(by 45 degrees) the threat image 
t1 = t1.crop((0,150,250,380))
t1 = t1.rotate(45)
t1 = t1.crop((5,90,220,160)) #(had to crop two times because otherwise rotation was not possible)

#adjusting threat image to blend with the background image
t1.putalpha(127)
t1 = ImageEnhance.Color(t1).enhance(3.5)
t1 = ImageEnhance.Contrast(t1).enhance(3.5)

#removing white background to make threat image transparent
t1 = t1.convert("RGBA")
datas = t1.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

t1.putdata(newData)

#overlaying the threat image on the background image
t1=t1.resize((90,30))
bag1.paste(t1, (70,120), t1.convert("RGBA"))

#displaying final output
plt.imshow(bag1)
bag1.save("BAG1.jpg")


# SECOND SET


#importing second background(bag2) and threat image(t2)
bag2 = Image.open('background_images/bg2.jpg')
t2 = Image.open('threat_images/t2.jpg')

#croping and rotating(by 45 degrees) the threat image 
t2 = t2.crop((0,370,160,560))
t2 = t2.rotate(45)
t2 = t2.crop((4,80,160,136))


#adjusting threat image to blend with the background image
t2.putalpha(127)
t2 = ImageEnhance.Contrast(t2).enhance(6.5)
t2 = ImageEnhance.Sharpness(t2).enhance(4.5)


#removing white background to make threat image transparent
t2 = t2.convert("RGBA")
datas = t2.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

t2.putdata(newData)

#overlaying the threat image on the background image
t2=t2.resize((100,40))
bag2.paste(t2, (160,50), t2.convert("RGBA"))

#displaying final output
plt.imshow(bag2)

bag2.save("BAG2.jpg")


# THIRD SET


#importing third background(bag3) and threat image(t3)
bag3 = Image.open('background_images/bg3.jpg')
t3 = Image.open('threat_images/t3.jpg')

#croping and rotating(by 45 degrees) the threat image 
t3=t3.crop((0,350,250,800))
t3=t3.rotate(45)
t3=t3.crop((0,250,250,360))


#adjusting threat image to blend with the background image
t3.putalpha(127)
t3 = ImageEnhance.Color(t3).enhance(4.5)
t3 = ImageEnhance.Contrast(t3).enhance(2.5)
t3 = ImageEnhance.Sharpness(t3).enhance(1.5)
t3 = ImageEnhance.Brightness(t3).enhance(1.5)

#removing white background to make threat image transparent
t3 = t3.convert("RGBA")
datas = t3.getdata()

newData = []
for item in datas:
    if (item[0] == 255 and item[1] == 255 and item[2] == 255) or (item[0] == 0 and item[1] == 0 and item[2] == 0):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

t3.putdata(newData)


#overlaying the threat image on the background image
t3 = t3.resize((250,100))
bag3.paste(t3, (360,360), t3.convert("RGBA"))


#displaying final output
plt.imshow(bag3)

bag3.save("BAG3.jpg")


# FORTH SET


#importing forth background(bag4) and threat image(t4)
bag4 = Image.open('background_images/bg4.jpg')
t4 = Image.open('threat_images/t4.jpg')

#croping and rotating(by 45 degrees) the threat image 
t4 = t4.crop((-10,50,280,450))
t4 = t4.rotate(45)
t4 = t4.crop((25,25,200,370))


#adjusting threat image to blend with the background image
t4.putalpha(127)
t4 = ImageEnhance.Color(t4).enhance(2.5)
t4 = ImageEnhance.Contrast(t4).enhance(2)
t4 = ImageEnhance.Sharpness(t4).enhance(1.5)

#removing white background to make threat image transparent
t4 = t4.convert("RGBA")
datas = t4.getdata()

newData = []
for item in datas:
    if (item[0] == 255 and item[1] == 255 and item[2] == 255) or (item[0] == 0 and item[1] == 0 and item[2] == 0):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

t4.putdata(newData)


#overlaying the threat image on the background image
t4=t4.resize((90,180))
bag4.paste(t4, (800,160), t4.convert("RGBA"))


#displaying final output
plt.imshow(bag4)

bag4.save("BAG4.jpg")


# FIFTH SET


#importing fifth background(bag5) and threat image(t5)
bag5 = Image.open('background_images/bg5.jpg')
t5 = Image.open('threat_images/t5.jpg')

#croping and rotating(by 45 degrees) the threat image 
t5 = t5.crop((0,440,400,800))
t5 = t5.rotate(45)
t5 = t5.crop((5,120,325,260))


#adjusting threat image to blend with the background image
t5.putalpha(127)
t5 = ImageEnhance.Contrast(t5).enhance(3.2)

#removing white background to make threat image transparent
t5 = t5.convert("RGBA")
datas = t5.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

t5.putdata(newData)

#overlaying the threat image on the background image
bag5.paste(t5, (140,120), t5.convert("RGBA"))

#displaying final output
plt.imshow(bag5)

bag5.save("BAG5.jpg")




