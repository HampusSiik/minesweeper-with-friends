# Flask app setup
from flask import Flask, session
from flask_socketio import SocketIO
from os import environ
from typing import Dict

from minesweeper_room.roomapi import RoomAPI
from minesweeper_room.player import Player


DEBUG = bool(int(environ.get("DEBUG", True)))
if DEBUG:
    SECRET_KEY = "my_secret"
    CORS_ALLOWED_ORIGINS = "*"
else:
    SECRET_KEY = environ.get("SECRET_KEY", "my_secret")
    CORS_ALLOWED_ORIGINS = environ.get("CORS_ALLOWED_ORIGINS", "127.0.0.1")

app = Flask(__name__)
"""
The `app` object is the Flask application that handles HTTP requests.
"""

app.config["SECRET_KEY"] = SECRET_KEY

socketio = SocketIO(app, cors_allowed_origins=CORS_ALLOWED_ORIGINS)
"""
The `socketio` object is the Flask-SocketIO extension that handles WebSocket connections.
"""

room_api = RoomAPI()
"""
The `room_api` object is the RoomAPI object that handles the room creation and management.
"""

players: Dict[str, Player] = {}
"""
The `players` dictionary maps usernames to player objects.
"""

from .endpoints import *
from .socketio_events import *
