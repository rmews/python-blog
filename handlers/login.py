from handlers.blog import BlogHandler
from models.user import User


class LoginHandler(BlogHandler):
    # Render log-in template
    def get(self):
        self.render('login.html')

    def post(self):
        # Variables from form.
        username = self.request.get('username')
        password = self.request.get('password')
        # Check db to see if username and password exsists.
        u = User.login(username, password)
        # If user input from form matches db, then redirect to home.
        if u:
            self.login(u)
            self.redirect('/')
        # If user form doesn't match db, then render form again with error.
        else:
            error = 'Invalid Login! Please check your username and password.'
            self.render('login.html', error=error)
