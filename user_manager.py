# user_manager.py

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QCheckBox, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QTextEdit, QWidget
from user import User
from userdao import UserDao

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(1200, 650, 600, 400)

# edit controls for the user
txt_name = QTextEdit(window)
txt_name.setGeometry(350, 50, 120, 30)
txt_email = QTextEdit(window)
txt_email.setGeometry(350, 90, 120, 30)
chk_active = QCheckBox(window)
chk_active.setGeometry(350, 130, 50, 30)

btn_save = QPushButton("Save", window)
btn_save.setGeometry(350, 170, 70, 30)

def on_save_clicked():
    # read the values
    updated_name = txt_name.toPlainText()
    updated_email = txt_email.toPlainText()
    selected_item = user_list.currentItem()
    selected_user = selected_item.data(Qt.ItemDataRole.UserRole)

    user_to_update = User(selected_user.id, updated_name, updated_email, False)
    dao.update(user_to_update)
    
    # update the listbox text and object
    selected_item.setText(updated_name)
    selected_item.setData(Qt.ItemDataRole.UserRole, user_to_update)

btn_save.clicked.connect(on_save_clicked)

user_list = QListWidget(window)
user_list.move(50, 50)

dao = UserDao()

users = dao.get_all()

for user in users:
    list_item = QListWidgetItem(user.name)
    list_item.setData(Qt.ItemDataRole.UserRole, user)
    user_list.addItem(list_item)

def on_list_item_clicked(item):
    clicked_user = item.data(Qt.ItemDataRole.UserRole)

    txt_name.setText(clicked_user.name)
    txt_email.setText(clicked_user.email)
    chk_active.setChecked(clicked_user.active)
    
user_list.itemClicked.connect(on_list_item_clicked)

window.show()
app.exec()