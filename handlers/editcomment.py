from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *


class EditCommentHandler(BlogHandler):
    def get(self, post_id, post_user_id, comment_id):
        # Render html if user is log-in and user matches user who made comment.
        if self.user and self.user.key().id() == int(post_user_id):
            postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
            comment = db.get(key)
            self.render('editcomment.html', content=comment.content)
        # Redirect to login if user is not logged-in.
        elif not self.user:
            self.redirect('/login')
        else:
            self.write("You don't have permission to edit this comment.")

    def post(self, post_id, post_user_id, comment_id):
        # Redirect to login if user is not logged-in.
        if not self.user:
            return self.redirect('/login')
        # If user is logged-in and user made post, store form data in variable.
        if self.user and self.user.key().id() == int(post_user_id):
            content = self.request.get('content')
            # If content was filled out on form, then post to db.
            if content:
                postKey = db.Key.from_path('Post',
                                           int(post_id),
                                           parent=blog_key())
                key = db.Key.from_path('Comment',
                                       int(comment_id),
                                       parent=postKey)
                comment = db.get(key)
                comment.content = content
                comment.put()
                self.redirect('/' + post_id)
            # If content is present, then render page with error message.
            else:
                error = "Please enter content!"
                self.render("editcomment.html",
                            content=content,
                            error=error)
        else:
            self.write("You don't have permission to edit this comment.")
