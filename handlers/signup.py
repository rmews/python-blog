from handlers.blog import BlogHandler
from models.user import User
from helpers import *


class SignupHandler(BlogHandler):
    def done(self):
        u = User.by_name(self.username)
        # As last check, see if username already exists before posting.
        if u:
            error = 'That user already exists.'
            self.render('signup.html', error_username=error)
        # If no error, register user and redirect to welcome page.
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            self.login(u)
            self.redirect('/welcome')

    # Render the sign-up form.
    def get(self):
        self.render('signup.html')

    def post(self):
        have_error = False
        # Get variables from form.
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username=self.username,
                      email=self.email)

        # Throw errors if form inputs are not valid.
        if not valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        # Render page with appropriate error message.
        if have_error:
            self.render('signup.html', **params)
        # If no form errors, finish.
        else:
            self.done()
