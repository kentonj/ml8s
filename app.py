"""Import the create_app (application factory), and set a variable named `application` to the function call."""
from src import create_app
# setting this variable to `application` allows gunicorn to pick it up automatically
application = create_app()
