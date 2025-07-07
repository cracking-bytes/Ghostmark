import numpy as np
import os
from PIL import Image

def lsb(path):
    print(f"\nAnalyzing image: {os.path.basename(path)}")

    img = Image.open(path).convert("RGB")
    extract = np.array(img)

    lsb_info = extract & 1
    flat_bit = lsb_info.flatten()

    zero = np.count_nonzero(flat_bit == 0)
    one = np.count_nonzero(flat_bit == 1)
    sum = zero + one

    percentofzero = (zero / sum) * 100
    percentofone = (one / sum) * 100
    diff = abs(percentofzero - percentofone)
    max = 5.0

    print(f"Total LSB's: {sum}")
    print(f"0s: {zero} ({percentofzero:.2f}%), 1s: {one} ({percentofone:.2f}%)")

    if diff < max:
        print("LSB looks normal (sensible)")
    else:
        print(f"Odd LSB's detected (difference: {diff:.2f}%)")
        if percentofzero > percentofone:
            print("0s > 1s — might be compression/hidden data")
        else:
            print("1s < 0s — unbalanced, possible steganography")

def chi2test(path):
    print("\nRunning chi-square test....")

    img = Image.open(path).convert("L")
    pixels = np.array(img).flatten()

    chi2 = 0.0
    valid_pairs = 0

    for i in range(0, 256, 2):
        tol_even = np.count_nonzero(pixels == i)
        odd = np.count_nonzero(pixels == i + 1)
        pair_total = tol_even + odd

        if pair_total > 0:
            expected = pair_total / 2
            chi2 += ((tol_even - expected) ** 2 + (odd - expected) ** 2) / expected
            valid_pairs += 1

    if valid_pairs > 0:
        chi2 /= valid_pairs

    print(f"Chi-square Score: {chi2:.2f}")

    if chi2 < 50:
        print("Confidence: Very High — might be hidden data")
    elif chi2 < 200:
        print("Confidence: High — possibly hidden data")
    elif chi2 < 500:
        print("Confidence: Medium — suspicious")
    elif chi2 < 1000:
        print("Confidence: Low — may be clean")
    else:
        print("Confidence: Very Low — image looks clean")

def img_path():
    while True:
        path = input("Enter path of the img: ").strip()
        if os.path.exists(path):
            return path
        else:
            print("404 - image not found.")

def main():
    print("=" * 50)
    print("Ghostmark - Steganography Detection Tool")
    print("=" * 50)

    check = img_path()
    print("\nStarting Test...\n")

    try:
        lsb(check)
        chi2test(check)

        print("\nConclusion:")
        print("✔ LSB's: Detects bit-level annomalys")
        print("✔ Chi-square test: Flags statistical anomalies")
        print("✔ Uses results together to decide data hiding")

    except Exception as e:
        print(f"error: {e}")

    print("\nAnalysis complete.")
    print("=" * 50)

if __name__ == "__main__":
    main()
