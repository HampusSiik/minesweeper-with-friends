# Flask app setup
from flask import Flask
from flask_socketio import SocketIO
from os import environ

from minesweeper_room.roomapi import RoomAPI


DEBUG = bool(int(environ.get("DEBUG", True)))
if DEBUG:
    SECRET_KEY = "my_secret"
    CORS_ALLOWED_ORIGINS = "*"
else:
    SECRET_KEY = environ.get("SECRET_KEY", "my_secret")
    CORS_ALLOWED_ORIGINS = environ.get("CORS_ALLOWED_ORIGINS", "127.0.0.1")

app = Flask(__name__)
"""
The `app` object is the Flask application that will handle HTTP requests.
"""

app.config["SECRET_KEY"] = SECRET_KEY

socketio = SocketIO(app, cors_allowed_origins=CORS_ALLOWED_ORIGINS)
"""
The `socketio` object is the Flask-SocketIO extension that will handle WebSocket connections.
"""

room_api = RoomAPI()
"""
The `room_api` object is the RoomAPI object that will handle the room creation and management.
"""

from .endpoints import *
from .socketio_events import *
