# consoledb.py


from userdao import UserDao


dao = UserDao()

for id in range(36, 40):
    dao.delete(id)

users = dao.get_all()

for user in users:
    print (user)

dao.close()

