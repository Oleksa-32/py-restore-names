import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
        ),
        (
            [
                {"first_name": None, "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": "Jane", "last_name": "Doe",
                 "full_name": "Jane Doe"},
            ],
            [
                {"first_name": "John", "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": "Jane", "last_name": "Doe",
                 "full_name": "Jane Doe"},
            ],
        ),
        (
            [
                {"first_name": None, "last_name": "Smith",
                 "full_name": "Alice Smith"},
                {"first_name": None, "last_name": "Smith",
                 "full_name": "Bob Smith"},
            ],
            [
                {"first_name": "Alice", "last_name": "Smith",
                 "full_name": "Alice Smith"},
                {"first_name": "Bob", "last_name": "Smith",
                 "full_name": "Bob Smith"},
            ],
        ),
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
