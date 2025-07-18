import os
import zipfile
import py7zr
import subprocess
from PIL import Image

def check_magic_number(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(8)
        if magic.startswith(b'\xFF\xD8\xFF'):
            return "JPEG"
        elif magic.startswith(b'\x89PNG\r\n\x1a\n'):
            return "PNG"
        elif magic.startswith(b'PK\x03\x04'):
            return "ZIP"
        elif magic.startswith(b'Rar!'):
            return "RAR"
        elif magic.startswith(b'7z\xBC\xAF\x27\x1C'):
            return "7Z"
        else:
            return "Unknown"

def try_open_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except:
        print("Image could not be opened. Might be encrypted or corrupted.")
        return False

def check_zip_password(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            for file in zf.infolist():
                if file.flag_bits & 0x1:
                    print("ZIP file is password protected.")
                    return True
        return False
    except:
        print("ZIP file could not be opened.")
        return False

def check_7z_password(file_path):
    try:
        with py7zr.SevenZipFile(file_path, mode='r', password="test") as archive:
            archive.getnames()
        return False
    except:
        print("7z file is password protected or unreadable.")
        return True

def check_metadata(file_path):
    try:
        result = subprocess.run(['./exiftool.exe', file_path], capture_output=True, text=True)
        metadata = result.stdout.strip()
        if not metadata:
            return
        lower = metadata.lower()
        if "password" in lower or "encrypted" in lower or "hidden" in lower:
            print("Metadata contains suspicious fields:")
            print("-" * 40)
            print(metadata)
            print("-" * 40)
    except:
        pass

def try_common_file_types(file_path):
    types = ['.txt', '.jpg', '.png', '.zip', '.7z']
    for ext in types:
        if ext == '.txt':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    print("File is a text file. Content:")
                    print("-" * 40)
                    print(text)
                    print("-" * 40)
                    return
            except:
                continue
        elif ext in ['.jpg', '.png']:
            if try_open_image(file_path):
                return
        elif ext == '.zip':
            check_zip_password(file_path)
            return
        elif ext == '.7z':
            check_7z_password(file_path)
            return

def analyze(file_path):
    kind = check_magic_number(file_path)
    if kind == "ZIP":
        check_zip_password(file_path)
    elif kind == "7Z":
        check_7z_password(file_path)
    elif kind in ["JPEG", "PNG"]:
        if not try_open_image(file_path):
            return
        check_metadata(file_path)
    elif kind == "RAR":
        print("RAR files are not supported.")
    else:
        try_common_file_types(file_path)

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    if not os.path.exists(path):
        print("File not found.")
    else:
        analyze(path)
