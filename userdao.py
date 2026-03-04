# userdao.py

import sqlite3

from user import User

class UserDao():

    def __init__(self, filename="C:\\work\\training\\databases\\userdb.db"):
        self.conn = sqlite3.connect(filename)

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
        pass
    def update(self, user):
        # update this user in the db
        pass
    
print ("UserDao tests")    
dao = UserDao()
users = dao.get_all()

for user in users:
    print (user)


