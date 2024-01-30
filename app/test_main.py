from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "check_url, connection, expected_result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "url has to be valid",
        "should have internet connection",
        "All correct",
        "url and internet connection has to be valid"
    ]
)
def test_valid_url_and_connection_exists(
        check_url: bool,
        connection: bool,
        expected_result: str
) -> None:
    with (mock.patch("app.main.valid_google_url", return_value=check_url),
          mock.patch(
              "app.main.has_internet_connection",
              return_value=connection)):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
