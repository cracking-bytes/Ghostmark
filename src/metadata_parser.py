from PIL import Image
import piexif
import pprint as prnt


def main(img_path):


    # img_path = input("Enter the image path: ")

    # checking for exif existence

    img = Image.open(img_path)

    exif_chk = img.info.keys()
    if "exif" not in img.info:
        print("No metadata found")
        exit()

    exif_d = piexif.load(img_path)

    #prnt.pprint(exif_dict)

    #sections

    sects = ['0th', 'Exif', 'GPS', 'Interop', '1st']

    for sect in sects:
        print(f"\n--- {sect} Metadata ---")

        if not exif_d[sect]:
            print("No data.")
            continue

        for t_id, value in exif_d[sect].items():
            t_info = piexif.TAGS[sect].get(t_id, {})
            t_name = t_info.get("name", f"Unknown({t_id})")

            

            # print(tag_info)
            # print(tag_name)

            if isinstance(value, bytes):
                try:
                    value = value.decode("utf-8", errors="ignore")
                except:
                    pass

            print(f"{t_name:30}: {value}")

