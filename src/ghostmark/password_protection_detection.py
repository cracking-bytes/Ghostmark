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

def check_extension_match(file_path, detected_type):
    ext = os.path.splitext(file_path)[1].lower().replace('.', '')
    ext_map = {
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png': 'PNG',
        'zip': 'ZIP',
        'rar': 'RAR',
        '7z': '7Z'
    }
    expected_type = ext_map.get(ext, 'Unknown')
    if expected_type != detected_type:
        print("Extension does not match actual file type.")
        print(f" - File Extension used: {expected_type}")
        print(f" - Actual file type: {detected_type}")
    else:
        print(f"File type identified as: {detected_type}")

def try_open_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        print("Image opened successfully [file not encrypted or corrupted]")
        return True
    except:
        print("Unable to open image [Might be encrypted or corrupted]")
        return False

def check_zip_password(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            for file in zf.infolist():
                if file.flag_bits & 0x1:
                    print("ZIP file is password protected.")
                    return True
        print("ZIP file is not password protected.")
        return False
    except:
        print("Unable to open ZIP file.")
        return False

def check_7z_password(file_path):
    try:
        with py7zr.SevenZipFile(file_path, mode='r', password="test") as archive:
            archive.getnames()
        print("7z file is not password protected.")
        return False
    except:
        print("7z file is password protected or unreadable.")
        return True

# def check_metadata(file_path):
#     try:
#         result = subprocess.run(['./exiftool.exe', file_path], capture_output=True, text=True)
#         metadata = result.stdout.strip()
#         if not metadata:
#             print("No metadata found.")
#             return

#         lines = metadata.splitlines()
#         useful_metadata = []

#         ignored_keywords = [
#             'dpi', 'resolution', 'software', 'colorspace', 'bits', 'compression',
#             'image width', 'image height', 'file type', 'exif version', 'megapixels',
#             'file size', 'mime type', 'encoding', 'samples', 'profile', 'gamma',
#             'interlace', 'color type', 'bit depth', 'filter', 'image size',
#             'directory', 'file name', 'exiftool version', 'permissions',
#             'modification date', 'access date', 'creation date'
#         ]

#         for line in lines:
#             lower_line = line.lower()
#             if any(keyword in lower_line for keyword in ignored_keywords):
#                 continue
#             useful_metadata.append(line)

#         if useful_metadata:
#             print("Non-default metadata fields detected:")
#             print("-" * 40)
#             for line in useful_metadata:
#                 print(line)
#             print("-" * 40)
#         else:
#             print("No suspicious metadata fields found...")

#     except:
#         print("Could not read metadata using ExifTool.")

def try_common_file_types(file_path):
    types = ['.txt', '.jpg', '.png', '.zip', '.7z']
    for ext in types:
        if ext == '.txt':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    print("Text file content:")
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
    print("Unknown or unsupported file type.")

def analyze(file_path):
    detected_type = check_magic_number(file_path)
    check_extension_match(file_path, detected_type)

    if detected_type == "ZIP":
        check_zip_password(file_path)
    elif detected_type == "7Z":
        check_7z_password(file_path)
    # elif detected_type in ["JPEG", "PNG"]:
    #     if try_open_image(file_path):
    #         check_metadata(file_path)
    elif detected_type == "RAR":
        print("RAR files are not supported.")
    else:
        try_common_file_types(file_path)

def main(img_path):
    if not os.path.exists(img_path):
        print("File not found.")
    else:
        analyze(img_path)
