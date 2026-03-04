# userdao.py

class UserDao():
    def get_all(self):
        # return all users from the db
        pass

    def add(self, user):
        # add this user to the db
        pass

    def delete(self, id):
        # delete user id from the db
        pass

    def update(self, user):
        # update this user in the db
        pass
    
dao = UserDao()
users = dao.get_all()

#for user in users:
#    print (user.name)


