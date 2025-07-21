from PIL import Image

def main(path):
    # path = input("Enter Image File Path:")
    img = Image.open(path)
    img = img.convert("RGB")
    pixals = img.load()

    width,height = img.size
    bit_stream = ''
    idk = 0
    found = False

    for y in range(height):
        for x in range (width):
            r ,g ,b = pixals[x, y]
            lsb = r & 1
            bit_stream += str(lsb)

            if "1111111111111110" in bit_stream:
                print("Message found!")
                # print(bit_stream)
                bit_stream = bit_stream.split("1111111111111110")[0]
                binary_msg = [bit_stream[i:i+8] for i in range(0, len(bit_stream),8)]
                message = ''.join([chr(int(b, 2)) for b in binary_msg])
                # print("Binary Chunks:", binary_msg)
                print("\nHidden Message:", message)
                found = True
                break

    
        if found:
            break

    if not found:
        print("No message found.")

# main(input(": "))