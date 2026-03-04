# userdao.py
import sqlite3
from user import User

class UserDao:
    def __init__(self, filename="C:\\work\\training\\databases\\userdb.db"):
        self.conn = sqlite3.connect(filename)

    def close(self):
        self.conn.close()

    def get_all(self):
        # return all users from the db
        users = []
        sql = "SELECT * FROM users"
        cur = self.conn.execute(sql)
        for rec in cur:
            id, name, email, active = rec
            user = User(id, name, email, bool(active))
            users.append(user)
        return users

    def add(self, user: User) -> User:
        # add this user to the db
        sql = """INSERT INTO users
                 (name, email, active)
                 VALUES(?,?,?)"""
        cur = self.conn.execute(sql, (user.name, user.email, 1 if user.active else 0))
        self.conn.commit()
        # get the id of the newly added user
        newid = cur.lastrowid if cur.lastrowid else 0
        # return a user object including the id
        return User(newid, user.name, user.email, user.active)

    def delete(self, id: int):
        # delete user id from the db
        sql = f"DELETE FROM users WHERE id={id}"
        self.conn.execute(sql)
        self.conn.commit()

    def update(self, user: User):
        # update this user in the db
        sql = """UPDATE users
                 SET name = ?,
                     email= ?,
                     active= ?
                 WHERE id = ?"""
        self.conn.execute(sql, (user.name, user.email, 1 if user.active else 0, user.id))
        self.conn.commit()

if __name__ == "__main__":
    print("UserDao tests")
    dao = UserDao()
    new_user = User(name="new", email="nu@gmail.com", active=False)
    added_user = dao.add(new_user)
    print(added_user)
    users = dao.get_all()
    if users:
        print(users[0])
        user_to_update = users[0]
        user_to_update.name = "changed"
        user_to_update.email = "changed@gmail.com"
        user_to_update.active = not user_to_update.active
        dao.update(user_to_update)
        users = dao.get_all()
        for user in users:
            print(user)
    dao.close()
