from system.core.controller import *
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC2db6fbfa88c487d653aebe5ddb673719" 
AUTH_TOKEN = "d97bff1471f311a1bb386b1fe5f0348a" 

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')


    def index(self):
        return self.load_view('landing_page.html')
    def main(self):
        return self.load_view('index.html')
    def confirmation(self, sessionid, userid):
        print sessionid
        print userid
        return self.load_view('confirmation.html', sessionid=sessionid, userid=userid)

    def create(self):
        print "hello create"
        user_info = {
             "full_name" : request.form['full_name'],
             "user_name" : request.form['user_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "pw_confirmation" : request.form['confirm_pass']
        }
        create_status = self.models['User'].create_user(user_info)
        print create_status
        if create_status['status'] == True:
            session['id'] = create_status['user']['id'] 
            session['full_name'] = create_status['user']['full_name']
            session['user_name'] = create_status['user']['user_name']
            session['email'] = create_status['user']['email']
            session['password'] = create_status['user']['pw_hash']
            
            return redirect('/info')
            # return redirect('/')
            # return redirect('/success')
        else:
            for message in create_status['errors']:
                flash(message, 'you have errors!')
            return redirect('/main')


    def info(self):
        user = self.models['User'].get_users()
        return self.load_view('user_list.html', user=user)


    def profile(self, id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('profile.html', user=user[0])

    def messages(self, id):
        user = self.models['User'].get_message(id)
        print user
        return self.load_view('messages.html', user=user)

    def send_message(self, sessionid, userid):
        print request.form['send_message']
        info={
            'messages': request.form['send_message'],
            'session_id': sessionid,
            'user_id': userid
        }
        print info
        self.models['User'].send_message(info)
        return redirect ('/info')

    def update_profile(self, id):
        info={
            'description': request.form['update_profile'],
            'user_id': session['id']
        }
        self.models['User'].update_profile(info)
        return redirect ('/profile/{}'.format(id))

    def login(self):
        print request.form['email']
        login_info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        print login_info
        user_login = self.models['User'].login_user(login_info)
        if user_login['status'] == True:
            session['email'] = user_login['user']['email']
            session['id'] = user_login['user']['id']
            return redirect('/info')
        else:
            for message in user_login['errors']:
                flash(message,'errors')
            return redirect('/main')