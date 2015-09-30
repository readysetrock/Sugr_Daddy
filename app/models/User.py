
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['full_name']:
            errors.append('Full Name cannot be blank')
        elif len(info['full_name']) < 2:
            errors.append('Full Name must be at least 2 characters long')

        if not info['user_name']:
            errors.append('User Name cannot be blank')
        elif len(info['user_name']) < 2:
            errors.append('Last Name must be at least 2 characters long')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')

        if not info['phone_number']:
            errors.append('Phone Number cannot be blank')
        elif len(info['phone_number']) != 10:
            errors.append('Phone Number must be 10 characters long')

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 3:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')

        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = 'INSERT INTO users (full_name, user_name, email, phone_number, pw_hash, created_at, updated_at) VALUES ("{}", "{}", "{}", "{}", "{}", NOW(), NOW())'.format(info['full_name'], info['user_name'], info['email'], info['phone_number'], hashed_pw)
            self.db.query_db(query)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

            # Then retrieve the last inserted user.
            # get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            # users = self.db.query_db(get_user_query)
            # return { "status": True, "user": users[0] }

    def get_users(self):
        query = 'SELECT * FROM users'
        return self.db.query_db(query)

    def get_user_by_id(self, id):
        query = 'SELECT * FROM users WHERE id="{}"'.format(id)
        return self.db.query_db(query)

    def login_user(self, info):
        password = info['password']
        user_query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(info['email'])
        # user_data = (info['email'])
        users = self.db.query_db(user_query)
        if users[0]:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(users[0]['pw_hash'], password):
                return { 
                "status": True, 
                "user": users[0] 
                }


        # Whether we did not find the email, or if the password did not match, either way return False
        return False
