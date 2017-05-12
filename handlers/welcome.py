from google.appengine.ext import db
from handlers.blog import BlogHandler


class WelcomeHandler(BlogHandler):
    # Render the welcome page if user is succesfully registered.
    def get(self):
        if self.user:
            self.render('welcome.html', username=self.user.name)
        # Redirect to signup page if non-user tries to access page.
        else:
            self.redirect('/signup')
