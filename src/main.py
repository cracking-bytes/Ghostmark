import os


# image input

def get_img_inp():
    while True:
        try:
            print("\nSelect input type: ")
            print("1. Single image")
            print("2. Multiple images")

            img_inp = int(input("Enter 1 or 2: ").strip())

            if img_inp == 1:
                img_path = input("Enter the path of the image: ").strip()
                return [img_path]
            elif img_inp == 2:
                img_path = input("Enter paths of images (comma-seperated): ").strip()
                img_list = [path.strip() for path in img_path.split(',') if path.strip()]
                return img_list
            else:
                print("⚠️ Please Enter 1 or 2 only.")
        except ValueError:
            print("❌ Invalid input! Please enter a number (1 or 2).")

images = get_img_inp()
print("images: ", images)


# feature select

def feature_select():
    while True:
        try:
            print('''\nPlease select what you want to do with the image/images:
1. Extract metadata
2. Detect Steganography
3. Extract Text (OCR)
4. Generate Image Hash
5. Wipe metadata
6. Detect Password Protection
7. All''')
            
            f_inp = input("Enter the numbers of the features you want to select (comma-seperated): ").strip()
            
            f_list = [int(i.strip()) for i in f_inp.split(',')]

            
            if all(1 <= i <= 7 for i in f_list):
                return f_list
                break
            else:
                print("❌ Please enter valid numbers between 1 and 7.\n")
            
        except ValueError:
            print("❌ Invalid input. Please enter numbers only, separated by commas.\n")


features = feature_select()

#metadata

if (i == 1 for i in features):
    from src.metadata_parser import extract_metadata

    for img_path in images:
        meta = extract_metadata(img_path)
        print(meta)