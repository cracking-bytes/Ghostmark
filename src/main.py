import os

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


