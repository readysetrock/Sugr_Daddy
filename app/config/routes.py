from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/create'] = 'Users#create'
routes['POST']['/login'] = 'Users#login'