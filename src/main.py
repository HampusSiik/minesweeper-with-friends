#!/usr/bin/env python

from minesweeper_api.api_app import app, socketio


def main():
    socketio.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
