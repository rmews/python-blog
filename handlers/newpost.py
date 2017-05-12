from handlers.blog import BlogHandler
from models.post import Post
from helpers import *


class NewPostHandler(BlogHandler):
    # Confirm log-in and render new post otherwise redirect to log-in
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    # Confirm new post by checking input fields & log-in
    def post(self):
        if not self.user:
            return self.redirect('/login')
        # Values pulled from new post template form
        subject = self.request.get('subject')
        content = self.request.get('content')

        # Check if subject and content fields are complete
        if subject and content:
            p = Post(parent=blog_key(),
                     subject=subject,
                     content=content,
                     user_id=self.user.key().id())
            # Stores Post parameters into the Google App database
            p.put()
            # Redirect to the post-id url fetched from datastore
            self.redirect('/%s' % str(p.key().id()))
        # Throw error and re-render page with subject, content and error
        else:
            error = "Please complete all fields."
            self.render("newpost.html",
                        subject=subject,
                        content=content,
                        error=error)
