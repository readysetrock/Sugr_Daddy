
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

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 3:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = 'INSERT INTO users (full_name, user_name, email, pw_hash, created_at, updated_at) VALUES (%s,%s,%s,%s, NOW(), NOW())'
            data=[info['full_name'], info['user_name'], info['email'], hashed_pw]
            self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def get_users(self):
        query = 'SELECT * FROM users'
        return self.db.query_db(query)

    def get_user_by_id(self, id):
        query = 'SELECT * FROM users WHERE id="{}"'.format(id)
        return self.db.query_db(query)

    def get_message(self, id):
        query='SELECT user_name, messages FROM users LEFT JOIN messages ON users.id=messages.session_id WHERE messages.user_id="{}"'.format(id)
        return self.db.query_db(query)

    def send_message(self, info):
        query='INSERT INTO messages (session_id, user_id, messages, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())'
        data=[info['session_id'], info['user_id'], info['messages']]
        return self.db.query_db(query, data)

    def update_profile(self, info):
        query='UPDATE users SET description= %s, updated_at=NOW() WHERE id=%s'
        data=[info['description'],info['user_id']]
        return self.db.query_db(query, data)

    def login_user(self, login_info):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        errors = []

        if not login_info['email']:
            errors.append('E-mail field required!')
        elif not EMAIL_REGEX.match(login_info['email']):
            errors.append('Pease enter a valid e-mail address!')

        if not login_info['password']:
            errors.append('Password field required!')
        if errors:
            return {'status': False, 'errors': errors}
        else:
            password = login_info['password']
            user_query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(login_info['email'])
            users = self.db.query_db(user_query)
            if users[0]:
                if self.bcrypt.check_password_hash(users[0]['pw_hash'], password):
                    return { 
                    "status": True, 
                    "user": users[0] 
                    }
                else:
                    errors.append('Password incorrect!')
                    return {'status': False, 'errors': errors}
