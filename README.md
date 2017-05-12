# Python Multi User Blog

A simple multi user blog where users can register to post blog posts as well as 'Like' and 'Comment' on other posts made on the blog.

## Framework
* jinja2 python templating and convience methods.
* App is built using Google App Engine and Datastore.
* MVC app architecture with everything seperated into routes, models, views and controllers (handlers). Very modular!

## Site Features
* Users can register, log-in and log-out
* User authentication using Set-Cookie method and hmac password hashing. Passwords are appropriately checked during login.
* Logged in users can create, edit, or delete blog posts they themselves have created. Users can only like posts once and cannot like their own post.
* Only signed in users can post comments. Users can only edit and delete comments they themselves have made.
* Logged out users are redirected to the login page when attempting to create, edit, delete, or like a blog post.
* All forms validate for user input
* Mobile first approach using Bootstrap v3

## Usage
Clone this repo to your desktop, go to its root directory (that contains the app.yaml) and run:
```bash
dev_appserver.py app.yaml
```

### Google App Engine Tips
* `gcloud init` start configuration of gcloud
* `gcloud app deploy --help` for detailed info on deployment and commands
* `gcloud app deploy` to deploy application to the Cloud Platform
* `gcloud app browse` to open the application via the browser on the command line
* Docs on deployment through python (https://cloud.google.com/appengine/docs/flexible/python/testing-and-deploying-your-app)

## Release History
* 1.0.0 - Initial release