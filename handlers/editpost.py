from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *


class EditPostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        # Render html if user is log-in and user matches user who made post.
        if self.user and self.user.key().id() == post.user_id:
            self.render('editpost.html',
                        subject=post.subject,
                        content=post.content,
                        post_id=post_id)
        # Redirect to login if user is not logged-in.
        elif not self.user:
            self.redirect('/login')
        else:
            self.write("You may only edit your own posts!")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        # Redirect to login if user is not logged-in.
        if not self.user:
            return self.redirect('/login')
        # If user is logged-in and user made comment, store form data.
        if self.user and self.user.key().id() == post.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')
            # If subject and content was filled out on form, then post to db.
            if subject and content:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                post.subject = subject
                post.content = content
                post.put()
                self.redirect('/%s' % str(post.key().id()))
            # If no subject or content, then render page with error message.
            else:
                error = "Please enter a subject and content!"
                self.render("editpost.html",
                            subject=subject,
                            content=content,
                            error=error)
        else:
            self.write("You may only edit your own posts!")
