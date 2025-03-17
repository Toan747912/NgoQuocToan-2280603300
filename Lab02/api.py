from cipher.transposition import TranspositionCipher
from flask import Flask, request, jsonify

# Khởi tạo Flask App
app = Flask(__name__)
transposition_cipher = TranspositionCipher()


@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')  # Sửa cú pháp gọi hàm
    key = int(data.get('key'))  # Sửa cú pháp gọi hàm
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')  # Sửa cú pháp gọi hàm
    key = int(data.get('key'))  # Sửa cú pháp gọi hàm
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
