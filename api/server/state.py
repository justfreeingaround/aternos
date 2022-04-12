from .endpoints import (
    SERVER_CREATE,
    SERVER_EULA,
    SERVER_RESTART,
    SERVER_START,
    SERVER_STOP,
)
import re

SERVER_ID = re.compile(r'var UID = "(.+?)"')


def start(session, *, headstart="0", access_credits="0"):

    session.xhr("POST", SERVER_EULA)

    return session.xhr(
        "POST",
        SERVER_START,
        params={"headstart": headstart, "access-credits": access_credits},
    ).json()


def stop(session):
    return session.xhr("POST", SERVER_STOP).json()


def restart(session):
    return session.xhr("POST", SERVER_RESTART).json()


def create(session, subdomain, motd, *, icon="https://aternos.org/panel/img/server-icon.php", software="java", timezone="UTC"):
    return session.xhr(
        "POST",
        SERVER_CREATE,
        data={
            "subdomain": subdomain,
            "motd": "§7{}".format(motd),
            "icon": icon,
            "software": software,
            "timezone": timezone,
        },
    ).json()


def fetch(session):
    return SERVER_ID.search(session.get("https://aternos.org/server/").text).group(1)
