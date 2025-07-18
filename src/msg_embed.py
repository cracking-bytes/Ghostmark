from PIL import Image


path = input("Enter Image File Path:\n")
msg = input("Enter Message you want to embed in image file: ")


msg_ascii = [ord(text) for text in msg]
ascii_to_bin = [format(char, '08b') for char in msg_ascii]
ascii_to_bin.append("1111111111111110") 
binary_message = ''.join(ascii_to_bin)

print("Binary to embed:", binary_message)

img = Image.open(path).convert("RGB")
pixels = img.load()
width, height = img.size

idx = 0
for y in range(height):
    for x in range(width):
        if idx < len(binary_message):
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary_message[idx])  
            pixels[x, y] = (r, g, b)
            idx += 1
        else:
            break
    if idx >= len(binary_message):
        break

img.save("tmp.png")
print("Message embedded and saved to tmp.png")
