import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)

    # Chuyển ảnh sang chế độ RGB nếu cần
    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Dấu hiệu kết thúc

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Lấy pixel dưới dạng list (R, G, B)

            for color_channel in range(3):  # Lặp qua R, G, B
                if data_index < len(binary_message):
                    # Chèn 1 bit vào kênh màu
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))  # Cập nhật pixel mới

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        sys.exit(1)

    image_path = sys.argv[1]
    message = sys.argv[2]

    encode_image(image_path, message)

if __name__ == "__main__":
    main()
