from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment
from helpers import *


class AddCommentHandler(BlogHandler):
    # Confirm log-in and render comment template otherwise redirect to login.
    def get(self, post_id, user_id):
        if self.user:
            self.render('addcomment.html')
        else:
            self.redirect('/login')

    # Confirm new post by checking log-in.
    def post(self, post_id, user_id):
        if not self.user:
            return self.redirect('/login')

        # Value pulled from comment template form.
        content = self.request.get('content')
        # Username value from User db.
        user_name = self.user.name
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # Check if variables are set and post to db.
        if content and user_name and key:
            c = Comment(parent=key,
                        user_id=int(user_id),
                        content=content,
                        user_name=user_name)
            c.put()
            self.redirect('/' + post_id)
        # If variables are not set throw error and render form again.
        else:
            error = "Please enter a comment."
            self.render('addcomment.html',
                        content=content,
                        error=error)
