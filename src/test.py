# import exifread
# from PIL.ExifTags import TAGS
# from PIL import Image


# print("1")
# with open("src/notes.txt", 'r') as notes:
#     content = notes.read()
#     #print(content)


# print("2")
# with open("src/43.jpg", 'rb') as img:
#     data = img.read(64)
#     print(data)

# print("3")
# with open("src/45.png", 'rb') as img1:
#     data2 = exifread.process_file(img1)
#     print(data2)

# print("4")
# img2 = Image.open("src/43.jpg")
# exif_data = img2._getexif()
# print(exif_data)

# import subprocess

# def extract_metadata(path):
#     result = subprocess.run(['exiftool', path], capture_output=True, text=True)
#     print(result.stdout)

# extract_metadata("src/45.png")




dict = {1:"cracking", 2:"bytes"}

for i, j in dict.items():
    print(i,j)
