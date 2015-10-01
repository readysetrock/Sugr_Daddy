from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/create'] = 'Users#create'
routes['POST']['/login'] = 'Users#login'
routes['/info']='Users#info'
routes['/profile/<id>']='Users#profile'
routes['/messages/<id>']='Users#messages'