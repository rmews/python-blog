from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.like import Like


class UnlikePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        # Post variable to regenerate front page with posts.
        posts = db.GqlQuery(
            "select * from Post order by created desc limit 10")
        # Render front again with error if user tries to unlike thier own post.
        if self.user and self.user.key().id() == post.user_id:
            error = "Sorry, you cannot unlike your own post."
            self.render('front.html',
                        posts=posts,
                        access_error=error)
        elif not self.user:
            self.redirect('/login')
        else:
            user_id = self.user.key().id()
            post_id = post.key().id()
            # Filter to see which posts a user has already liked.
            l = Like.all().filter('user_id =', user_id).filter(
                                  'post_id =', post_id).get()
            # Remove like value by 1 and render post page again.
            if l:
                l.delete()
                post.likes -= 1
                post.put()
                self.redirect('/' + str(post.key().id()))
            else:
                self.redirect('/' + str(post.key().id()))
