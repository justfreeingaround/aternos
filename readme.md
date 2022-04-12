<h1 align="center">Aternos API</h1>

<p align="center">
A full scale API to ease up the interaction with the Aternos server.
</p>

<p align="center">
This API, in any way shape or form, is not made for begineer users.
</p>

<p align="center">
<b>You need to use the internal HTTP client for interacting with the functions correctly. The <code>.xhr</code> method automatically solves the parameters and fetches your endeavors for you.</b>
</p>

<h3>Usage:</h3>

You need to first, build a clear authorisation pathway to the API. This can be done via `.login` or `.signup` methods. The internal session will automatically handle the cookies, **however**, these functions will also return your session cookie.

```py

from api.http_client import AternosClient
from api.authflow import signup
from api.server import state

client = AternosClient(follow_redirects=True)

username = "username"
password = "password"

authflow.signup(client, username, password) # Optional [kwargs: `email`]

state.create(
    client,
    subdomain=username,
    motd="An automated world!"
) # Optional [kwargs: `icon`, `software`, `timezone`]


state.start(client)

# Console websocket @ wss://aternos.org/hermes/
# Sending `{"stream":"console","type":"start"}`
# with the appropriate cookies will create a console
# connection.
```

Currently, the "software" selection is not implemented as that seems to be a hectic task.
