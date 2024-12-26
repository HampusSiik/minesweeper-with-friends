#!/usr/bin/env python3.13

from os import environ

from minesweeper_api.api_app import app, socketio

DEBUG = bool(int(environ.get("DEBUG", True)))

ADDRESS = "0.0.0.0"
PORT = 5000

if not DEBUG:
    ADDRESS = environ.get("ADDRESS", "0.0.0.0")
    PORT = int(environ.get("PORT", 80))


def main():
    socketio.run(
        app,
        host=ADDRESS,
        port=PORT,
        debug=DEBUG,
    )


if __name__ == "__main__":
    main()
