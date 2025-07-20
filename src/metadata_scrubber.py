from PIL import Image
import piexif

def main(img_path):


    # img_path = input("Enter the image path: ")

    #checking for EXIF

    img = Image.open(img_path)

    exif_chk = img.info.keys()
    if "exif" not in img.info:
        print("No metadata found to scrub")
        exit()

    exif_d = piexif.load(img_path)

    sects = ['0th', 'Exif', 'GPS', 'Interop', '1st']

    for sect in sects:
        print(f"\nScrubbing {sect} Metadata...")
        exif_d[sect] = {}

    imgsave = input(f"\nEnter the path with name of the image when saved (example: example_images/clean.jpg or leave empty): ")

    if imgsave == "":
        imgsave = "img_clean.jpg"

    exif_bi = piexif.dump(exif_d)
    img.save(imgsave, "jpeg", exif = exif_bi)
