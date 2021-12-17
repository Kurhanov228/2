from PIL import Image

image = Image.open("monro.jpg")
RGB_image = image.convert("RGB")
print(RGB_image.mode)  # Вернуло CMYK, значит канала 4
red, green, blue = RGB_image.split()
red.save("monro_red.jpg")
green.save("monro_green.jpg")
blue.save("monro_blue.jpg")

coordinates = (100, 0, image.width, image.height) #  Красная
cropped = red.crop(coordinates)
cropped.save("monro_nalotgino.jpg")
cods2=(50, 0, image.width-50, image.height)
cropped2 = red.crop(cods2)
cropped2.save("monro_3.0.jpg")
imagesvo = Image.blend(cropped, cropped2, 0.5)
imagesvo.save("Monro_gotovo.jpg")

coordinatesblue = (0, 0, image.width-100, image.height) # Синия
croppedblue1 = blue.crop(coordinatesblue)
croppedblue1.save("monro_naloginoblue.jpg")
codsblue=(50, 0, image.width-50, image.height)
croppedblue = blue.crop(codsblue)
croppedblue.save("monro_vo.jpg")
imagesvoblue = Image.blend(croppedblue1, croppedblue, 0.5)
imagesvoblue.save("Monro_vooo.jpg")

coordinatesgreen = (50, 0, image.width-50, image.height) # Зелёная
croppedgreeen = green.crop(coordinatesgreen)
croppedgreeen.save("monro_naloginogreen.jpg")

new_image = Image.merge("RGB", (imagesvo,croppedgreeen,imagesvoblue))# Соед
new_image.save("monro_realitog.jpg")
new_image.thumbnail((80,80))
new_image.save("manro_small.jpg")
