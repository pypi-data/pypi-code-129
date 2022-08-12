from app import app

from .subscriber import Subscriber
with app.app_context():
    sub = Subscriber(app)
    sub.setup()

