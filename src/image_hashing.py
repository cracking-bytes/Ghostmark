from PIL import Image
import hashlib as hl
import imagehash as ih


def main(img):
    with open(img, 'rb') as img1a:
        data = img1a.read()
        # print(data)

    sha256_hash = hl.sha256(data).hexdigest()
    md5_hash = hl.md5(data).hexdigest()

    print("\n --- Cryptographic hashes ---")
    print(f"SHA256 : {sha256_hash}")
    print(f"MD5    : {md5_hash}")

    print("\n --- Perceptual Hashes ---")

    img1b = Image.open(img)
    ahash = ih.average_hash(img1b)
    dhash = ih.dhash(img1b)
    phash = ih.phash(img1b)

    print("aHash :", ahash)
    print("dHash :", dhash)
    print("pHash :", phash)

    return {
        "sha256": sha256_hash,
        "md5": md5_hash,
        "ahash": ahash,
        "dhash": dhash,
        "phash": phash
    }

def compare(h1, h2):
    print("\n --- Comparision Result ---")
    print()

    #sha256
    if h1['sha256'] == h2['sha256']:
        print("SHA256: Images are exactly the same.")
    else:
        print("SHA256: Images are different at the binary level.")

    #md5
    if h1['md5'] == h2['md5']:
        print("MD5: Images are exactly the same.")
    else:
        print("MD5: Images are different at the binary level.")

    #ahash
    if h1['ahash'] - h2['ahash'] <= 5:
        print("aHash: Images look visually similar.")
    else:
        print("aHash: Images look different.")

    #dhash
    if h1['dhash'] - h2['dhash'] <= 5:
        print("dHash: Images look visually similar.")
    else:
        print("dHash: Images look different.")

    #phash
    if h1['phash'] - h2['phash'] <= 5:
        print("pHash: Images look visually similar.")
    else:
        print("pHash: Images look different.")

    

img1 = 'example_images/img.jpg'
print("Image 1:")
h1 = main(img1)

print()

img2 = 'example_images/clean.jpg'
print("Image 2:")
h2 = main(img2)

compare(h1,h2)

