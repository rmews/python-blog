import os
import re
import hmac
import jinja2
import hashlib
import random

from string import letters
from google.appengine.ext import db

# Jinja configuration
# Templates to be fetched from templates directory & HTML escape = True
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# Global functions
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


# Model keys
def users_key(group='default'):
    return db.Key.from_path('users', group)


# Store blog key to Google Data that defines a parent attribute
def blog_key(name='default'):
    return db.Key.from_path('blogs', name)

# Validation
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


def valid_username(username):
    return username and USER_RE.match(username)


def valid_password(password):
    return password and PASS_RE.match(password)


def valid_email(email):
    return not email or EMAIL_RE.match(email)

# Authentication
secret = '!"qmd}he-[U$)bA[&BeWh:./fqv)?d=TJU,bN6=B'


# Create password hash using sha256
def make_pw_hash(name, password, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + password + salt).hexdigest()
    return '%s,%s' % (salt, h)


# Randomly generate 5 letter string used as salt
def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))


# Verify if a user's password matches it's hash
def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)


# Create secure hmac hash cookie
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


# Check to see if cookie is secure
def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val
