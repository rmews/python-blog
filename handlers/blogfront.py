from google.appengine.ext import db
from handlers.blog import BlogHandler


class BlogFrontHandler(BlogHandler):
    def get(self):
        # Look up all posts by creation time and display latest 10.
        posts = db.GqlQuery(
            "select * from Post order by created desc limit 10")
        # Render those posts to front template.
        self.render('front.html', posts=posts)
