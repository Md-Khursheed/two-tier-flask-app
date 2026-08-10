import json
from unittest.mock import patch, MagicMock

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("app.mysql")
def test_hello_route_returns_200(mock_mysql, client):
    """GET / should render the page with whatever messages the DB returns."""
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [("hello world",)]
    mock_mysql.connection.cursor.return_value = mock_cursor

    response = client.get("/")

    assert response.status_code == 200
    mock_cursor.execute.assert_called_once_with("SELECT message FROM messages")


@patch("app.mysql")
def test_submit_route_inserts_message(mock_mysql, client):
    """POST /submit should insert the message and echo it back as JSON."""
    mock_cursor = MagicMock()
    mock_mysql.connection.cursor.return_value = mock_cursor

    response = client.post("/submit", data={"new_message": "test message"})

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "test message"
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO messages (message) VALUES (%s)", ["test message"]
    )
    mock_mysql.connection.commit.assert_called_once()


@patch("app.mysql")
def test_submit_route_with_no_message(mock_mysql, client):
    """POST /submit with no form field should still return 200, message as None."""
    mock_cursor = MagicMock()
    mock_mysql.connection.cursor.return_value = mock_cursor

    response = client.post("/submit", data={})

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] is None
