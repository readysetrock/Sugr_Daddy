from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/create'] = 'Users#create'
routes['POST']['/login'] = 'Users#login'
routes['/info']='Users#info'
routes['/profile/<id>']='Users#profile'
routes['/messages/<id>']='Users#messages'
routes['/main']='Users#main'
routes['POST']['/send_message/<sessionid>/<userid>']='Users#send_message'
routes['GET']['/confirmation/<sessionid>/<userid>']='Users#confirmation'
routes['POST']['/update_profile/<id>']='Users#update_profile'


