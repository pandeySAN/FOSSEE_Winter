import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout
import matplotlib.pyplot as plt
from api import upload

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")

        layout = QVBoxLayout()

        self.btn = QPushButton("Upload CSV")
        self.btn.clicked.connect(self.upload_file)
        layout.addWidget(self.btn)

        self.label = QLabel("Upload a file to see summary.")
        layout.addWidget(self.label)

        self.setLayout(layout)

    def upload_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open CSV")
        if path:
            data = upload(path)
            self.label.setText(str(data))

            # plot
            plt.bar(data["type_distribution"].keys(),
                    data["type_distribution"].values())
            plt.title("Equipment Type Distribution")
            plt.show()

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
