#!/usr/bin/env python

from os import environ

from minesweeper_api.api_app import app, socketio


def main():
    socketio.run(
        app,
        host=environ.get("ADDRESS", "0.0.0.0"),
        port=environ.get("PORT", 5000),
        debug=environ.get("DEBUG", True),
    )


if __name__ == "__main__":
    main()
