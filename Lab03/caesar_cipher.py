import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút với chức năng
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        plain_text = self.ui.textEdit.toPlainText().strip()
        key = self.ui.lineEdit.text().strip()

        if not plain_text or not key.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập văn bản và khóa hợp lệ.")
            return

        payload = {"plain_text": plain_text, "key": int(key)}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Thành công", "Mã hóa thành công!")
            else:
                QMessageBox.warning(self, "Lỗi API", f"Lỗi: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Lỗi: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        cipher_text = self.ui.plainTextEdit.toPlainText().strip()
        key = self.ui.lineEdit.text().strip()

        if not cipher_text or not key.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập văn bản mã hóa và khóa hợp lệ.")
            return

        payload = {"cipher_text": cipher_text, "key": int(key)}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setPlainText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Thành công", "Giải mã thành công!")
            else:
                QMessageBox.warning(self, "Lỗi API", f"Lỗi: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Lỗi: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
