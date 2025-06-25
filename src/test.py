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




import exifread

def exifread_extract(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        print(f"\n[Exifread] Metadata for {image_path}:")
        if tags:
            for tag in tags:
                print(f"{tag}: {tags[tag]}")
        else:
            print("No EXIF metadata found.")


from PIL import Image
from PIL.ExifTags import TAGS

def pillow_extract(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        print(f"\n[Pillow] Metadata for {image_path}:")
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                print(f"{tag}: {value}")
        else:
            print("No EXIF metadata found.")
    except Exception as e:
        print(f"Error reading image: {e}")


import subprocess

def exiftool_extract(image_path):
    result = subprocess.run(["exiftool", image_path], capture_output=True, text=True)
    print(f"\n[ExifTool] Metadata for {image_path}:\n{result.stdout}")


import exiftool

def pyexiftool_extract(image_path):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(image_path)
        print(f"\n[PyExifTool] Metadata for {image_path}:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
