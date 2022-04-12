from .endpoints import SERVER_SUBDOMAIN, SERVER_MOTD


def change_subdomain(session, subdomain):
    return session.xhr("GET", SERVER_SUBDOMAIN, params={"subdomain": subdomain}).json()


def change_motd(session, motd):
    return session.xhr("POST", SERVER_MOTD, data={"motd": "§7{}".format(motd)}).json()
