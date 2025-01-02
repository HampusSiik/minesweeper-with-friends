import unittest
from flask.app import AppContext
from flask_socketio import SocketIOTestClient
from flask.testing import FlaskClient
from minesweeper_api.api_app import (
    app,
    socketio,
    games,
)


class TestMinesweeperAPI(unittest.TestCase):

    app: FlaskClient
    socketio: SocketIOTestClient
    app_context: AppContext

    def setUp(self):
        """
        Set up the test client and other resources before each test.
        """
        self.app = app.test_client()
        self.socketio = socketio.test_client(app)
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        """
        Clean up after each test.
        """
        self.app_context.pop()
        games.clear()

    def test_create_game(self):
        """
        Test the `/create_game` endpoint.
        """
        data = {"rows": 5, "cols": 5, "mines": 5}
        response = self.app.post("/create_game", json=data)
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIn("game_id", response_json)
        game_id = response_json["game_id"]
        self.assertTrue(game_id.startswith("game_"))
        self.assertIn(game_id, games)

    def test_get_board(self):
        """
        Test the `/get_board/<game_id>` endpoint.
        """
        data = {"rows": 5, "cols": 5, "mines": 5}
        create_response = self.app.post("/create_game", json=data)
        game_id = create_response.get_json()["game_id"]

        response = self.app.get(f"/get_board/{game_id}")
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIn("board", response_json)

    def test_join_game(self):
        """
        Test the WebSocket 'join_game' event.
        """
        data = {"rows": 5, "cols": 5, "mines": 5}
        create_response = self.app.post("/create_game", json=data)
        game_id = create_response.get_json()["game_id"]

        self.socketio.emit("join_game", {"game_id": game_id})
        received = self.socketio.get_received()
        self.assertTrue(
            any(msg["args"]["msg"] == f"Player joined {game_id}" for msg in received)
        )

    def test_left_click(self):
        """
        Test the WebSocket 'left_click' event.
        """
        data = {"rows": 5, "cols": 5, "mines": 5}
        create_response = self.app.post("/create_game", json=data)
        game_id = create_response.get_json()["game_id"]

        position = {"row": 2, "col": 3}
        self.socketio.emit("join_game", {"game_id": game_id})
        self.socketio.emit("left_click", {"game_id": game_id, "position": position})

        received = self.socketio.get_received()
        self.assertTrue(any("update_board" in msg["name"] for msg in received))

    def test_right_click(self):
        """
        Test the WebSocket 'right_click' event.
        """
        data = {"rows": 5, "cols": 5, "mines": 5}
        create_response = self.app.post("/create_game", json=data)
        game_id = create_response.get_json()["game_id"]

        position = {"row": 2, "col": 3}
        self.socketio.emit("join_game", {"game_id": game_id})
        self.socketio.emit("right_click", {"game_id": game_id, "position": position})

        received = self.socketio.get_received()
        self.assertTrue(any("update_board" in msg["name"] for msg in received))


if __name__ == "__main__":
    unittest.main()
