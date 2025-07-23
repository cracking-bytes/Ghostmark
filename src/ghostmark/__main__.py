import os
from ghostmark import metadata_parser as mp
from ghostmark import metadata_scrubber as ms
from ghostmark import msg_embed as me
from ghostmark import text_extraction as te
from ghostmark import steganography_detection as sd
from ghostmark import image_hashing as ih
from ghostmark import password_protection_detection as ppd

def main():

    # image input

    # def get_img_inp():
    #     while True:
    #         try:
    #             print("\nSelect input type: ")
    #             print("1. Single image")
    #             print("2. Multiple images")

    #             img_inp = int(input("Enter 1 or 2: ").strip())

    #             if img_inp == 1:
    #                 img_path = input("Enter the path of the image: ").strip()
    #                 return [img_path]
    #             elif img_inp == 2:
    #                 img_path = input("Enter paths of images (comma-seperated): ").strip()
    #                 img_list = [path.strip() for path in img_path.split(',') if path.strip()]
    #                 return img_list
    #             else:
    #                 print("Please Enter 1 or 2 only.")
    #         except ValueError:
    #             print("Invalid input! Please enter a number (1 or 2).")

    # images = get_img_inp()
    # print("images: ", images)


    print(r'''
      _____ _               _                        _    
     / ____| |             | |                      | |   
    | |  __| |__   ___  ___| |_ _ __ ___   __ _ _ __| | __
    | | |_ | '_ \ / _ \/ __| __| '_ ` _ \ / _` | '__| |/ /
    | |__| | | | | (_) \__ \ |_| | | | | | (_| | |  |   < 
     \_____|_| |_|\___/|___/\__|_| |_| |_|\__,_|_|  |_|\_\
                                                        
                                                        
    ''')



    # # feature select

    def feature_select():
        while True:
            try:
                print('''\nPlease select what you want to do with the image:
    1. Extract metadata
    2. Wipe metadata
    3. Embed text in image
    4. Extract Hidden Text
    5. Steganography Detection
    6. Generate Image Hash
    7. Image comparision
    8. Detect Password Protection
    9. All''')
                
                f_inp = input("Enter the numbers of the features you want to select (comma-seperated): ").strip()
                
                f_list = [int(i.strip()) for i in f_inp.split(',')]

                
                if all(1 <= i <= 9 for i in f_list):
                    return f_list
                    break
                else:
                    print("Please enter valid numbers between 1 and 7.\n")
                
            except ValueError:
                print("Invalid input. Please enter numbers only, separated by commas.\n")



    # working of the features

    # def ext(img_path):
    #     return
    #     ext = os.path.splitext(img_path)[1].lower()


    def work(i, img_path):

        if i == 1:
            print('''\n\n\n--- Metadata Extraction ---\n''')

            if pathc == "n":
                img_path = input("Enter the image path: ").strip()
            mp.main(img_path)

        if i == 2:
            print("\n\n\n--- Metadata Scrubbing ---\n")
            if pathc == "n":
                img_path = input("Enter the image path: ").strip()
            ms.main(img_path)

        if i == 3:
            print("\n\n\n--- Embedding Text In An Image ---\n")
            if pathc == "n":
                img_path = input("Enter the image path: ").strip()
            me.main(img_path)

        if i == 4:
            print("\n\n\n--- Hidden Text Extraction ---\n")
            if pathc == "n":
                img_path = input("Enter the image path: ").strip()
            te.main(img_path)

        if i == 5:
            print("\n\n\n--- Steganography Detection ---")
            if pathc == "n":
                img_path = input("Enter the image path: ").strip()
            sd.main(img_path)
            
        if i == 6:
            print("\n\n\n--- Generated Image Hashes ---\n")
            if pathc == "n":
                img_path = input("Enter the image path: ")
            hashing = ih.hashing(img_path)
            for key, value in hashing.items():
                print(f"{key}: {value}")

        if i == 7:
            print("\n\n\n--- Image Comparision ---\n")
            if pathc == "n":
                img_path = input("Enter the first image path: ")
                img_path2 = input("Enter the second image path: \n")
            else:
                img_path2 = input("Enter the second image path: ")
            i1 = ih.hashing(img_path)
            i2 = ih.hashing(img_path2)
            ih.compare(i1, i2)

        if i == 8:
            print("\n\n\n--- Detecting Password Protection ---\n")
            if pathc == "n":
                img_path = input("Enter the image path: ")
            ppd.main(img_path)




    features = feature_select()

    if len(features) > 1 or 9 in features:
        while True:
            try:
                pathc = input("Do you want to use same img path for all selected features (y/n): ")
                
                if pathc == "y":
                    img_path = input("Enter the image path: ").strip()
                    break
                elif pathc == "n":
                    img_path = ''
                    break
                else:
                    print(" !! Please choose from yes (y) or no (n).\n")

            except ValueError:
                print("Invalid input. Please choose from yes (y) or no (n).\n")
    else:
        img_path = ''
        pathc = "n"



    if 9 in features:
        for i in range(1,9):
            work(i, img_path)
    else:
        for i in features:
            work(i, img_path)
        
if __name__ == "__main__":
    main()
