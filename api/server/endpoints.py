from ..endpoints import AJAX_PANEL

CONFIGURATION_ENDPOINT = AJAX_PANEL + "options/config.php"
IMAGE_ENDPOINT = AJAX_PANEL + "options/image.php"
TIMEZONE_ENDPOINT = AJAX_PANEL + "options/timezone.php"

SERVER_HOTLIST_ADD = AJAX_PANEL + "players/add.php"
SERVER_HOTLIST_REMOVE = AJAX_PANEL + "players/remove.php"


SERVER_SUBDOMAIN = AJAX_PANEL + "options/subdomain.php"
SERVER_MOTD = AJAX_PANEL + "options/motd.php"

SERVER_START = AJAX_PANEL + "start.php"
SERVER_STOP = AJAX_PANEL + "stop.php"
SERVER_EULA = AJAX_PANEL + "eula.php"
SERVER_RESTART = AJAX_PANEL + "restart.php"
SERVER_CREATE = AJAX_PANEL + "server/create.php"
