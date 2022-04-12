import random
import re
from functools import cached_property

import httpx


def random_string(length=16):
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))


TOKEN = re.compile(r"<script type='text/javascript'>(.+?)</script>")
TOKEN_ISOLATION = re.compile(r"\?(.+?):")
STRING_VALUE = re.compile(r'"(.+?)"')


class AternosClient(httpx.Client):
    def xhr(self, method, url, **kwargs):

        headers = kwargs.pop("headers", {})
        headers.update(
            {
                "X-Requested-With": "XMLHttpRequest",
            }
        )

        key, value = random_string(), random_string()

        params = kwargs.pop("params", {})
        params.update({"SEC": "{}:{}".format(key, value), "TOKEN": self.site_token})

        self.cookies.update({"ATERNOS_SEC_{}".format(key): value})
        return self.request(method, url, headers=headers, params=params, **kwargs)

    @cached_property
    def site_token(self):
        bearer = self.get("https://aternos.org/go/", follow_redirects=True).text

        token = TOKEN_ISOLATION.search(TOKEN.search(bearer).group(1)).group(1)
        string_values = STRING_VALUE.findall(token)

        if ".map(s => s.split('').reverse().join('')).join('')" in token:
            return "".join(_[::-1] for _ in string_values)

        if ".reverse().join('')" in token:
            return "".join(string_values[::-1])

        return "".join(string_values)
