# General
import webapp2
from google.appengine.ext import db
from helpers import *

# Models
from models.user import User
from models.post import Post
from models.like import Like
from models.comment import Comment


# Handlers
from handlers.blog import BlogHandler
from handlers.blogfront import BlogFrontHandler
from handlers.signup import SignupHandler
from handlers.welcome import WelcomeHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler
from handlers.post import PostHandler
from handlers.newpost import NewPostHandler
from handlers.editpost import EditPostHandler
from handlers.deletepost import DeletePostHandler
from handlers.likepost import LikePostHandler
from handlers.unlikepost import UnlikePostHandler
from handlers.addcomment import AddCommentHandler
from handlers.editcomment import EditCommentHandler
from handlers.deletecomment import DeleteCommentHandler


# Routing
app = webapp2.WSGIApplication([
    ('/', BlogFrontHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/newpost', NewPostHandler),
    ('/([0-9]+)', PostHandler),
    ('/([0-9]+)/like', LikePostHandler),
    ('/([0-9]+)/unlike', UnlikePostHandler),
    ('/([0-9]+)/edit', EditPostHandler),
    ('/([0-9]+)/delete/([0-9]+)', DeletePostHandler),
    ('/([0-9]+)/addcomment/([0-9]+)', AddCommentHandler),
    ('/([0-9]+)/([0-9]+)/editcomment/([0-9]+)', EditCommentHandler),
    ('/([0-9]+)/([0-9]+)/deletecomment/([0-9]+)', DeleteCommentHandler)
], debug=True)
