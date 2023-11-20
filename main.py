from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl

class IffHubApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IFF HUB")
        self.setGeometry(100, 100, 800, 600)

        # Add icon
        icon_path = "images/iffHub.png"
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

        # Main Label
        label = QLabel("IFF HUB", self)
        label.setStyleSheet("font-size: 14pt;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(10, 10, 780, 30)

        # Buttons with Icons
        button_frame = QWidget(self)
        button_frame.setGeometry(200, 30, 1280, 250)

        button1 = QPushButton("CoreDao", button_frame, clicked=self.button1_action)
        button1.setGeometry(10, 10, 180, 50)

        button2 = QPushButton("Ambion", button_frame, clicked=self.button2_action)
        button2.setGeometry(200, 10, 180, 50)

        button3 = QPushButton("MetaMask Accoutns", button_frame, clicked=self.button3_action)
        button3.setGeometry(10, 70, 180, 50)

        button4 = QPushButton("Connect Wallet Metamask", button_frame, clicked=self.button4_action)
        button4.setGeometry(200, 70, 180, 50)

        # Browser Button
        browser_button = QPushButton("Browser", button_frame, clicked=self.open_browser)
        browser_button.setGeometry(10, 130, 370, 50)

        # Bottom Text
        bottom_text = QLabel("iffHub.beta.1-0", self)
        bottom_text.setStyleSheet("font-size: 14pt;")
        bottom_text.setAlignment(Qt.AlignCenter)
        bottom_text.setGeometry(10, 520, 780, 30)

        # Create a QWebEngineView for displaying the browser
        self.browser_view = QWebEngineView(self)
        self.browser_view.setGeometry(10, 210, 1280, 750)

    def button1_action(self):
        print("Button 1 clicked")

    def button2_action(self):
        print("Button 2 clicked")

    def button3_action(self):
        print("Button 3 clicked")

    def button4_action(self):
        print("Button 4 clicked")

    def open_browser(self):
        url = "https://google.com"
        self.browser_view.setUrl(QUrl(url))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_window = IffHubApp()
    main_window.show()
    sys.exit(app.exec_())
