# Flask app setup
from flask import Flask
from flask_socketio import SocketIO
from os import environ
from typing import Dict
from minesweeper.game.minesweeper import Minesweeper

app = Flask(__name__)
"""
The `app` object is the Flask application that will handle HTTP requests.
"""
app.config["SECRET_KEY"] = environ.get("SECRET_KEY", "my_secret")
socketio = SocketIO(app, cors_allowed_origins=environ.get("CORS_ALLOWED_ORIGINS", "*"))
"""
The `socketio` object is the Flask-SocketIO extension that will handle WebSocket connections.
"""

games: Dict[str, Minesweeper] = {}
"""
The `games` dictionary stores the active Minesweeper games.
"""

from minesweeper_api.endpoints import *
from minesweeper_api.socketio_events import *
