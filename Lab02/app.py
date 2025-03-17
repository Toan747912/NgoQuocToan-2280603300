from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form.get('inputPlainText', '')  # Đọc đúng tên input
    key = request.form.get('inputKeyPlain', '0')   # Đọc đúng tên key

    try:
        key = int(key)
    except ValueError:
        return "Key phải là số nguyên!", 400  # Tránh lỗi nếu key không hợp lệ

    caesar_cipher = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form.get('inputCipherText', '')  # Đọc đúng tên input
    key = request.form.get('inputKeyCipher', '0')   # Đọc đúng tên key

    try:
        key = int(key)
    except ValueError:
        return "Key phải là số nguyên!", 400

    caesar_cipher = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
