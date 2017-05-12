from handlers.blog import BlogHandler


class LogoutHandler(BlogHandler):
    # Redirect user to home on logout.
    def get(self):
        self.logout()
        self.redirect('/')
