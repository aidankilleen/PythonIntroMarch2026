# userdao.py

import sqlite3

from user import User

class UserDao():

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
            user = User(id, name, email, active)
            users.append(user)

        return users

    def add(self, user):
        # add this user to the db
        pass
    def delete(self, id):
        # delete user id from the db
        sql = f"DELETE FROM users WHERE id={id}"
        self.conn.execute(sql)
        self.conn.commit()
        
    def update(self, user):
        # update this user in the db
        sql = f"""UPDATE users
                    SET name = ?, 
                        email= ?, 
                        active= ?
                    WHERE id = ?"""
        self.conn.execute(sql, 
            (user.name, user.email, 1 if user.active else 0, user.id))
        self.conn.commit()

    
print ("UserDao tests")    
dao = UserDao()

dao.delete(15)

users = dao.get_all()

print (users[-1])

user_to_update = users[-1]
user_to_update.name = "changed"
user_to_update.email = "changed@gmail.com"
user_to_update.active = not user_to_update.active

dao.update(user_to_update)

users = dao.get_all()

for user in users:
    print (user)


dao.close()