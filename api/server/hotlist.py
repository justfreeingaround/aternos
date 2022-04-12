import enum

from .endpoints import SERVER_HOTLIST_ADD, SERVER_HOTLIST_REMOVE


class Hotlist(enum.Enum):
    whitelist = "whitelist"
    banned_players = "banned-players"
    ops = "ops"
    banned_ips = "banned-ips"


def add_player(session, player, list_type=Hotlist.whitelist):

    if not isinstance(list_type, Hotlist):
        raise ValueError("List type must be a Hotlist")

    return session.xhr(
        "POST", SERVER_HOTLIST_ADD, data={"name": player, "list": list_type.value}
    )


def remove_player(session, player, list_type=Hotlist.whitelist):

    if not isinstance(list_type, Hotlist):
        raise ValueError("List type must be a Hotlist")

    return session.xhr(
        "POST", SERVER_HOTLIST_REMOVE, data={"name": player, "list": list_type.value}
    )
