from PIL import Image
import numpy as np
import time
import os

def extract_lsb(image_path):
    print(f"\n[🔍] Analyzing LSB in: {os.path.basename(image_path)}")
    img = Image.open(image_path)
    img = img.convert("RGB")
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

    # LSB analysis conclusion
    threshold = 5  # Percentage difference threshold
    diff = abs(zero_percent - one_percent)
    
    if diff < threshold:
        print("[✅] LSB Distribution: Balanced (normal for clean images)")
    else:
        print(f"[⚠️] LSB Distribution: Imbalanced (difference: {diff:.2f}%)")
        if zero_percent > one_percent:
            print("     - Excess of 0s may indicate hidden data or compression artifacts")
        else:
            print("     - Excess of 1s is unusual and strongly suggests data embedding")

def chi_square_test(image_path):
    print(f"\n[📊] Running Statistical Analysis (Chi-Square Test)")
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale
    pixels = np.array(img).flatten()

    chi_squared = 0
    valid_pairs = 0
    
    for i in range(0, 256, 2):
        count_even = np.count_nonzero(pixels == i)
        count_odd = np.count_nonzero(pixels == i + 1)
        total = count_even + count_odd
        
        if total > 0:
            valid_pairs += 1
            expected = total / 2
            chi_squared += ((count_even - expected) ** 2 + (count_odd - expected) ** 2) / expected

    # Normalize by number of valid pairs
    if valid_pairs > 0:
        chi_squared /= valid_pairs
    
    print(f"[⚖️] Chi-Square Score: {chi_squared:,.2f}")
    
    # Confidence interpretation
    if chi_squared < 50:
        confidence = "VERY HIGH"
        conclusion = "Almost certainly contains hidden data"
    elif chi_squared < 200:
        confidence = "HIGH"
        conclusion = "Likely contains hidden data"
    elif chi_squared < 500:
        confidence = "MODERATE"
        conclusion = "Suspicious, may contain hidden data"
    elif chi_squared < 1000:
        confidence = "LOW"
        conclusion = "Possibly clean, but warrants further inspection"
    else:
        confidence = "VERY LOW"
        conclusion = "Appears clean (normal image noise)"
    
    print(f"[📈] Confidence: {confidence}")
    print(f"[🔎] Conclusion: {conclusion}")

def get_image_path():
    while True:
        image_path = input("\nEnter the path of the image to analyze: ").strip()
        if os.path.exists(image_path):
            return image_path
        print(f"❌ File not found: {image_path}. Please try again.")

def main():
    print("═══════════════════════════════════════════════")
    print("👻 Ghostmark - Advanced Steganography Detector")
    print("═══════════════════════════════════════════════")
    
    # Get image path from user
    image_path = get_image_path()
    
    print("\n>>> Starting forensic analysis...\n")

    try:
        extract_lsb(image_path)
        chi_square_test(image_path)
        
        print("\n[📋] Final Assessment:")
        print("1. LSB analysis checks bit distribution anomalies")
        print("2. Chi-Square test detects statistical deviations")
        print("3. Combine both results for accurate detection")
        
    except Exception as e:
        print(f"[❌] Error analyzing image: {str(e)}")

    print("\n>>> Analysis complete.")
    print("═══════════════════════════════════════════════")

if __name__ == "__main__":
    main()