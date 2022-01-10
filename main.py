from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()

coordinates = (100, 0, image.width, image.height) #  Красная
cropped = red.crop(coordinates)
cods2=(50, 0, image.width-50, image.height)
cropped2 = red.crop(cods2)
imagesvo = Image.blend(cropped, cropped2, 0.5)

coordinatesblue = (0, 0, image.width-100, image.height) # Синия
croppedblue1 = blue.crop(coordinatesblue)
codsblue=(50, 0, image.width-50, image.height)
croppedblue = blue.crop(codsblue)
imagesvoblue = Image.blend(croppedblue1, croppedblue, 0.5)

coordinatesgreen = (50, 0, image.width-50, image.height) # Зелёная
croppedgreeen = green.crop(coordinatesgreen)

new_image = Image.merge("RGB", (imagesvo,croppedgreeen,imagesvoblue))# Соед
new_image.save("monro_realitog.jpg")
new_image.thumbnail((80,80))
new_image.save("manro_small.jpg")
