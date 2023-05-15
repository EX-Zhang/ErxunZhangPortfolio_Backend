
from bcrypt import gensalt, hashpw, checkpw

from enum import Enum

from .models import User

class User():

    def __init__(self,username,password,email=None):

        self.username = username

        if email == None:

            self.password = password

        else:

            self.password = hashpw(password, gensalt())

            self.email = email


    def check_password(self):

        users = User.objects.filter(username=self.username)

        if len(users) != 1:

            return UserStatus.InvalidUsername

        if not checkpw(self.password, users[0].password):

            return UserStatus.InvalidPassword

        return UserStatus.OK
        

    def register(self):

        if len(User.objects.filter(username=self.username)) != 0:

            return UserStatus.UsernameExisted

        User(username=self.username,password=self.password,email=self.email,admin=False).save()

        return UserStatus.OK

        
class UserStatus(Enum):

    OK = 0
    InvalidUsername = 1
    InvalidPassword = 2
    UsernameExisted = 3
