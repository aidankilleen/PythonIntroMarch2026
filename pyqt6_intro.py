# pyqt6_intro.py

from PyQt6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("PyQt6 Introduction")
window.setGeometry(1000, 450,600, 400)

btn = QPushButton("Press Me", window)
btn.move(50, 250)

def on_clicked():
    QMessageBox.information(window, "Clicked", "You clicked the button")

btn.clicked.connect(on_clicked)

lst = QListWidget(window)
lst.move(100, 30)

items = ["one", "two", "three"]

for item in items:

    lst.addItem(QListWidgetItem(item))


window.show()
app.exec()



