from PIL import Image, ExifTags

print("")
print("Daten die im Bild gefunden wurden:")
print("----------------------------------------")

img = Image.open("C:/Users/home/Bilder/Saved Pictures/Plakat/handy2020.jpg")
for i, j in img._getexif().items():
    if i in ExifTags.TAGS:
        print("")
        print(ExifTags.TAGS[i] + " - " + str(j))
