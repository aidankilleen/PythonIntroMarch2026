# user_manager.py
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QWidget,
    QLabel,
)
from user import User
from userdao import UserDao

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("User Manager")
window.setGeometry(1200, 650, 600, 400)

# Labels (minimal UI additions)
lbl_name = QLabel("Name:", window)
lbl_name.setGeometry(290, 50, 60, 30)

lbl_email = QLabel("Email:", window)
lbl_email.setGeometry(290, 90, 60, 30)

lbl_active = QLabel("Active:", window)
lbl_active.setGeometry(290, 130, 60, 30)

# Edit controls for the user (reuse existing widgets where possible)
txt_name = QTextEdit(window)
txt_name.setGeometry(350, 50, 200, 30)

txt_email = QTextEdit(window)
txt_email.setGeometry(350, 90, 200, 30)

chk_active = QCheckBox(window)
chk_active.setGeometry(350, 130, 50, 30)

btn_save = QPushButton("Save", window)
btn_save.setGeometry(350, 170, 90, 30)

# Small addition to ease creation flow (optional): a New button to clear the form
btn_new = QPushButton("New", window)
btn_new.setGeometry(450, 170, 90, 30)

user_list = QListWidget(window)
user_list.setGeometry(20, 20, 250, 320)

# DAO
dao = UserDao()

# Populate the list from DB
users = dao.get_all()
for user in users:
    list_item = QListWidgetItem(user.name)
    list_item.setData(Qt.ItemDataRole.UserRole, user)
    user_list.addItem(list_item)


def clear_form():
    """Clear the editor fields and deselect the list to indicate 'create new'."""
    txt_name.setText("")
    txt_email.setText("")
    chk_active.setChecked(False)
    user_list.clearSelection()


def on_list_item_clicked(item):
    clicked_user = item.data(Qt.ItemDataRole.UserRole)
    txt_name.setText(clicked_user.name)
    txt_email.setText(clicked_user.email)
    chk_active.setChecked(clicked_user.active)


user_list.itemClicked.connect(on_list_item_clicked)


def on_new_clicked():
    clear_form()


btn_new.clicked.connect(on_new_clicked)


def on_save_clicked():
    # Read values
    updated_name = txt_name.toPlainText().strip()
    updated_email = txt_email.toPlainText().strip()
    updated_active = chk_active.isChecked()

    # Basic validation
    if not updated_name or not updated_email:
        QMessageBox.warning(window, "Validation", "Both name and email are required.")
        return

    selected_item = user_list.currentItem()

    if selected_item is None:
        # Create new user
        new_user = User(name=updated_name, email=updated_email, active=updated_active)
        added_user = dao.add(new_user)

        # Update UI: add to list and select it
        list_item = QListWidgetItem(added_user.name)
        list_item.setData(Qt.ItemDataRole.UserRole, added_user)
        user_list.addItem(list_item)
        user_list.setCurrentItem(list_item)

        QMessageBox.information(window, "User Added", f"User '{added_user.name}' added (id={added_user.id}).")
    else:
        # Update existing user
        selected_user = selected_item.data(Qt.ItemDataRole.UserRole)
        user_to_update = User(selected_user.id, updated_name, updated_email, updated_active)
        dao.update(user_to_update)

        # Update the listbox text and object
        selected_item.setText(updated_name)
        selected_item.setData(Qt.ItemDataRole.UserRole, user_to_update)

        QMessageBox.information(window, "User Updated", f"User '{updated_name}' updated.")


btn_save.clicked.connect(on_save_clicked)

window.show()
app.exec()
