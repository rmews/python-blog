from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *


class DeleteCommentHandler(BlogHandler):
    def get(self, post_id, post_user_id, comment_id):
        # Check log-in status and verify user matches user who made comment.
        if self.user and self.user.key().id() == int(post_user_id):
            postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
            comment = db.get(key)
            comment.delete()
            self.redirect('/' + post_id)
        # Redirect to log-in if user not logged in.
        elif not self.user:
            self.redirect('/login')
        # Write error if not logged in.
        else:
            self.write("You don't have permission to delete this comment.")
