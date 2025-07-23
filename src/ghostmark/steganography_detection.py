import numpy as np
import os
from PIL import Image

def lsb(path):
    print(f"\nAnalyzing image: {os.path.basename(path)}")

    img = Image.open(path).convert("RGB")
    extract = np.array(img)

    channels = ['Red', 'Green', 'Blue']
    total_zero = total_one = 0

    for i, color in enumerate(channels):
        lsb_info = extract[:, :, i] & 1
        flat_bit = lsb_info.flatten()

        zero = np.count_nonzero(flat_bit == 0)
        one = np.count_nonzero(flat_bit == 1)
        total = zero + one

        total_zero += zero
        total_one += one

        percent_zero = (zero / total) * 100
        percent_one = (one / total) * 100
        diff = abs(percent_zero - percent_one)

        print(f"\n--- {color} Channel ---")
        print(f"Total LSBs: {total}")
        print(f"0s: {zero} ({percent_zero:.2f}%), 1s: {one} ({percent_one:.2f}%)")
        print(f"Difference: {diff:.2f}%")

    grand_total = total_zero + total_one
    avg_zero = (total_zero / grand_total) * 100
    avg_one = (total_one / grand_total) * 100
    avg_diff = abs(avg_zero - avg_one)

    print("\n--- Average Across All Channels ---")
    print(f"Total LSBs: {grand_total}")
    print(f"0s: {total_zero} ({avg_zero:.2f}%), 1s: {total_one} ({avg_one:.2f}%)")
    print(f"Difference: {avg_diff:.2f}%")

    print("\nThis is a statistical overview.")
    print("   Review the difference yourself to decide.")
    print("   If the difference is small (~<5%), data might be hidden.")

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

def img_path(path):
    while True:
        # path = input("Enter path of the img: ").strip()
        if os.path.exists(path):
            return path
        else:
            print("404 - image not found.")

def main(path):
    # print("=" * 50)
    # print("Ghostmark - Steganography Detection Tool")
    # print("=" * 50)

    check = img_path(path)
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

    print("\n\nAnalysis complete.")
    # print("=" * 50)

# if __name__ == "__main__":
#     main()
