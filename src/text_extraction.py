from PIL import Image
import numpy as np
import os

def extract_lsb_stats(image_path):
    print(f"\n[🔍] Analyzing LSB in: {os.path.basename(image_path)}")
    img = Image.open(image_path).convert("RGB")
    data = np.array(img)
    lsb_data = data & 1 
    flat_lsb = lsb_data.flatten()

    zeros = np.count_nonzero(flat_lsb == 0)
    ones = np.count_nonzero(flat_lsb == 1)
    total = zeros + ones
    zero_percent = (zeros / total) * 100
    one_percent = (ones / total) * 100

    print(f"[🧮] Extracted {total:,} LSB bits")
    print(f"[🔢] Distribution -> 0s: {zeros:,} ({zero_percent:.2f}%) | 1s: {ones:,} ({one_percent:.2f}%)")

    threshold = 5
    diff = abs(zero_percent - one_percent)

    if diff < threshold:
        print("[✅] LSB Distribution: Balanced (normal for clean images)")
        return False
    else:
        print(f"[⚠️] LSB Distribution: Imbalanced (difference: {diff:.2f}%)")
        return True  

def chi_square_test(image_path):
    print(f"\n[📊] Running Chi-Square Statistical Analysis")
    img = Image.open(image_path).convert("L")
    pixels = np.array(img).flatten()

    chi_squared = 0
    valid_pairs = 0

    for i in range(0, 256, 2):
        even = np.count_nonzero(pixels == i)
        odd = np.count_nonzero(pixels == i + 1)
        total = even + odd
        if total > 0:
            valid_pairs += 1
            expected = total / 2
            chi_squared += ((even - expected) ** 2 + (odd - expected) ** 2) / expected

    if valid_pairs > 0:
        chi_squared /= valid_pairs

    print(f"[⚖️] Chi-Square Score: {chi_squared:.2f}")

    if chi_squared < 50:
        print("[📈] Confidence: VERY HIGH - Hidden data almost certain")
        return True
    elif chi_squared < 200:
        print("[📈] Confidence: HIGH - Likely contains hidden data")
        return True
    elif chi_squared < 500:
        print("[📈] Confidence: MODERATE - Suspicious")
        return True
    else:
        print("[📈] Confidence: LOW/VERY LOW - Probably clean")
        return False

def extract_lsb_text(image_path):
    print(f"\n[📤] Attempting to extract text from LSBs...")
    img = Image.open(image_path).convert("RGB")
    bits = []

    for pixel in img.getdata():
        for channel in pixel[:3]: 
            bits.append(channel & 1)

    chars = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break
        byte = int("".join(str(bit) for bit in byte_bits), 2)
        if byte == 0:
            break
        chars.append(chr(byte))

    hidden_text = ''.join(chars)
    print(f"[📜] Hidden Text:\n{hidden_text if hidden_text else '[None Found]'}")
    return hidden_text

def get_image_path():
    while True:
        path = input("\nEnter PNG image path to analyze: ").strip()
        if os.path.exists(path):
            return path
        print("❌ File not found. Try again.")

def main():
    print("═══════════════════════════════════════════════")
    print("🧠 Ghostmark Text Extractor - LSB Text Analyzer")
    print("═══════════════════════════════════════════════")

    path = get_image_path()

    try:
        print("\n>>> Step 1: Running LSB & Chi Analysis...\n")
        suspicious = extract_lsb_stats(path) or chi_square_test(path)

        if suspicious:
            print("\n>>> Step 2: LSB anomaly found. Extracting hidden text...")
            extract_lsb_text(path)
        else:
            print("\n[🟢] No strong steganographic indicators. Extraction skipped.")

    except Exception as e:
        print(f"[❌] Error: {str(e)}")

    print("\n>>> Analysis complete.")
    print("═══════════════════════════════════════════════")

if __name__ == "__main__":
    main()
