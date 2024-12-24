#!/usr/bin/env python

from os import environ

from minesweeper_api.api_app import app, socketio

ADDRESS = environ.get("ADDRESS", "0.0.0.0")
PORT = int(environ.get("PORT", 5000))
DEBUG = bool(int(environ.get("DEBUG", True)))


def main():
    socketio.run(
        app,
        host=ADDRESS,
        port=PORT,
        debug=DEBUG,
    )


if __name__ == "__main__":
    main()
