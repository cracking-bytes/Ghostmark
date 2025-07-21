# Ghostmark

**Ghostmark** is a command-line toolkit designed with almost all features that you require for image forensics. It can extract metadata, scrub metadata, embed or extract text from the images, detect for steganography, generate image hashes and compare them, detect for password protection.

---

## Features

- Metadata Extraction
- Metadata Scrubber
- Embedding Text
- Extracting Hidden Text
- Steganography Detection
- Generating Image Hash
- Image Hash Comparision
- Detecting Password Protection
- CLI based

---

## Run Locally

Clone the project

```bash
git clone https://github.com/cracking-bytes/Ghostmark.git
```

Go to the project directory

```bash
cd Ghostmark
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the program (CLI)

```bash
python3 src/main.py
```

## Working

| Feature                | Supporting File Types | Saving File Type      |
|------------------------|-----------------------|-----------------------|
| Metadata Extraction    |  JPG                  |                       |
| Metadata Scrubber      |  JPG                  |  JPG, PNG             |
| Embedding Text         |  JPG, PNG             |  PNG                  |
| Extracting Hidden Text |  PNG                  |                       |
| Steganography Detection|  JPG, PNG             |                       |
| Generating Image Hash  |  JPG, PNG             |                       |
| Image Hash Comparison  |  JPG, PNG             |                       |
| Detecting Password Protection |   JPG, PNG     |                       |

---

## Tech Stack

**Language Used:**
- Python 3

**Libraries Used:**
- `pillow` 
- `piexif`
- `pprint`
- `hashlib`
- `imagehash`
- `numpy`
- `os`
- `zipfile`
- `py7zr`
- `subprocess`

**Dev Tools:**

- VS Code
- Git & GitHub for version control

---

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

## Authors

Bhavika Nagdeo (Cracking Bytes)  
- [GitHub](https://github.com/cracking-bytes)  
- [LinkedIn](https://in.linkedin.com/in/bhavikanagdeo)  
- [Instagram](https://www.instagram.com/cracking.bytes/)  
- [Medium](https://crackingbytes.medium.com/)

Ranveer
- [GitHub](https://github.com/Ranveerrrrr)
- [Linkedin](https://www.linkedin.com/in/ranveer-kohli-16ab76346)
- [Instagram](https://www.instagram.com/3ug_atsec)

---


## Feedback

If you have any feedback, ideas, or features to suggest, reach out at **bhavikanagdeo83@gmail.com**
