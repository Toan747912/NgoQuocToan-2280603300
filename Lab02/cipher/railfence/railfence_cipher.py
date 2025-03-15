class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text  # Nếu chỉ có 1 rail thì không cần mã hóa

        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # Xu hướng đi xuống

        for char in plain_text:
            rails[rail_index].append(char)

            # Đổi hướng khi chạm đáy hoặc chạm đỉnh
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text  # Nếu chỉ có 1 rail thì không cần giải mã

        # Bước 1: Xác định số ký tự trên mỗi rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in cipher_text:
            rail_lengths[rail_index] += 1

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # Bước 2: Chia chuỗi mã hóa thành các rail
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Bước 3: Đọc chữ cái theo đường zigzag
        plain_text = []
        rail_index = 0
        direction = 1

        for _ in cipher_text:
            plain_text.append(rails[rail_index].pop(0))

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return "".join(plain_text)
