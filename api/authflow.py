import json
from hashlib import md5

from .endpoints import (
    EMAIL_VALIDATION,
    SIGNUP_ENDPOINT,
    LOGIN_ENDPOINT,
    USERNAME_VALIDATION,
)


def validate_username(session, username):
    return session.xhr(
        "POST",
        USERNAME_VALIDATION,
        data={"username": username},
    ).json()["success"]


def validate_email(session, email):
    return session.xhr(
        "POST",
        EMAIL_VALIDATION,
        data={"email": email},
    ).json()["success"]


def signup(session, username, password, *, email=""):

    assert validate_username(
        session, username
    ), "Username is already taken or is invalid."

    return session.xhr(
        "POST",
        SIGNUP_ENDPOINT,
        data={
            "username": username,
            "account": json.dumps(
                {
                    "type": "email",
                    "email": email,
                    "password": md5(password.encode("utf-8")).hexdigest(),
                }
            ),
        },
    ).cookies.get("ATERNOS_SESSION")


def login(session, username, password):
    return session.xhr(
        "POST",
        LOGIN_ENDPOINT,
        data={
            "user": username,
            "password": md5(password.encode("utf-8")).hexdigest(),
        },
    ).cookies.get("ATERNOS_SESSION")
