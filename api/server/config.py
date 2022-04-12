from .endpoints import CONFIGURATION_ENDPOINT, TIMEZONE_ENDPOINT, IMAGE_ENDPOINT


true_aliases = ["on", "true", "yes", "t", "y", True]
false_aliases = ["off", "false", "no", "f", "n", False]


class Options:
    def __init__(self):

        self._gamemode = "survival"
        self._max_players = 20
        self._difficulty = "easy"
        self._whitelist = False
        self._cracked = False
        self._pvp = True
        self._force_gamemode = False
        self._commandblocks = True
        self._animals = True
        self._monster = True
        self._villagers = True
        self._nether = True
        self._spawn_protection = 0
        self._resource_pack_required = False
        self._resource_pack = ""
        self._flight = True

    @property
    def gamemode(self):
        return self._gamemode

    @gamemode.setter
    def gamemode(self, value):
        assert value in [
            "survival",
            "creative",
            "adventure",
            "spectator",
        ], "Gamemode must be one of: survival, creative, adventure, spectator"
        self._gamemode = value

    @property
    def max_players(self):
        return self._max_players

    @max_players.setter
    def max_players(self, value):
        assert isinstance(value, int), "Max players must be an integer"
        self._max_players = value

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        assert value in [
            "peaceful",
            "easy",
            "normal",
            "hard",
        ], "Difficulty must be one of: peaceful, easy, normal, hard"
        self._difficulty = value

    @property
    def whitelist(self):
        return self._whitelist

    @whitelist.setter
    def whitelist(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Whitelist must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._whitelist = value in true_aliases

    @property
    def cracked(self):
        return self._cracked

    @cracked.setter
    def cracked(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Cracked state must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._cracked = value in true_aliases

    @property
    def pvp(self):
        return self._pvp

    @pvp.setter
    def pvp(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "PVP state must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._pvp = value in true_aliases

    @property
    def force_gamemode(self):
        return self._force_gamemode

    @force_gamemode.setter
    def force_gamemode(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Force gamemode state must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._force_gamemode = value in true_aliases

    @property
    def commandblocks(self):
        return self._commandblocks

    @commandblocks.setter
    def commandblocks(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Command blocks state must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._commandblocks = value in true_aliases

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Animals spawning must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._animals = value in true_aliases

    @property
    def monster(self):
        return self._monster

    @monster.setter
    def monster(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Monster spawning must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._monster = value in true_aliases

    @property
    def villagers(self):
        return self._villagers

    @villagers.setter
    def villagers(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Villagers spawning must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._villagers = value in true_aliases

    @property
    def nether(self):
        return self._nether

    @nether.setter
    def nether(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Nether must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._nether = value in true_aliases

    @property
    def spawn_protection(self):
        return self._spawn_protection

    @spawn_protection.setter
    def spawn_protection(self, value):
        assert isinstance(value, int), "Spawn protection must be an integer"
        self._spawn_protection = value

    @property
    def resource_pack_required(self):
        return self._resource_pack_required

    @resource_pack_required.setter
    def resource_pack_required(self, value):
        if not isinstance(value, bool) and value not in true_aliases + false_aliases:
            raise ValueError(
                "Resource pack requirement must be a boolean or one of: "
                + ", ".join(true_aliases + false_aliases)
            )

        self._resource_pack_required = value in true_aliases

    @property
    def resource_pack(self):
        return self._resource_pack

    @resource_pack.setter
    def resource_pack(self, value):
        assert isinstance(value, str), "Resource pack must be a string"
        self._resource_pack = value

    def export(self):
        """
        Exports the world to a dictionary.
        """
        return {
            "gamemode": self.gamemode,
            "max-players": self.max_players,
            "difficulty": self.difficulty,
            "white-list": self.whitelist,
            "online-mode": self.cracked,
            "pvp": self.pvp,
            "force-gamemode": self.force_gamemode,
            "enable-command-block": self.commandblocks,
            "spawn-animals": self.animals,
            "spawn-monster": self.monster,
            "spawn-npcs": self.villagers,
            "allow-nether": self.nether,
            "spawn-protection": self.spawn_protection,
            "require-resource-pack": self.resource_pack_required,
            "resource-pack": self.resource_pack,
        }


def set_configuration(session, configuration: Options):

    state = {}

    for key, value in configuration.export().items():
        state[key] = session.xhr(
            "POST",
            CONFIGURATION_ENDPOINT,
            data={"file": "/server.properties", "options": key, "value": value},
        ).json()

    return state


def set_timezone(session, timezone="UTC"):
    return session.xhr("POST", TIMEZONE_ENDPOINT, data={"timezone": timezone}).json()


def set_image(session, image):

    assert image in ["openjdk:17", "ibm-semeru-runtimes:open-17-jre"], "Invalid image"

    return session.xhr("POST", IMAGE_ENDPOINT, data={"image": image}).json()
