# Flask app setup
from flask import Flask
from flask_socketio import SocketIO
from os import environ
from typing import Dict
from minesweeper.game.minesweeper import Minesweeper


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

games: Dict[str, Minesweeper] = {}
"""
The `games` dictionary stores the active Minesweeper games.
"""

from minesweeper_api.endpoints import *
from minesweeper_api.socketio_events import *
