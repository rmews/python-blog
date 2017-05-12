from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.like import Like


class LikePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        # Post variable to regenerate front page with posts.
        posts = db.GqlQuery(
            "select * from Post order by created desc limit 10")
        # Render front again with error if user tries to like thier own post.
        if self.user and self.user.key().id() == post.user_id:
            error = "Sorry, you cannot like your own post."
            self.render('front.html',
                        posts=posts,
                        access_error=error)
        elif not self.user:
            self.redirect('/login')
        else:
            user_id = self.user.key().id()
            post_id = post.key().id()
            # Filter to see which posts a user has already liked.
            like = Like.all().filter('user_id =', user_id).filter(
                                    'post_id =', post_id).get()
            # If user already liked post, then render page again with error.
            if like:
                comments = db.GqlQuery(
                    "select * from Comment where ancestor is :1 "
                    "order by created desc limit 10", key)
                error = "You cannot like a post more than once"
                self.render("permalink.html",
                            post=post,
                            comments=comments,
                            like_error=error)
            # If user has not liked post, then +1 like count.
            else:
                like = Like(parent=key,
                            user_id=self.user.key().id(),
                            post_id=post.key().id())
                post.likes += 1
                like.put()
                post.put()
                self.redirect('/' + str(post.key().id()))
