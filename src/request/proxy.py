#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2021 Ygor Simões

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from src.core.color import Color
from requests import get


class Proxy:

    def __init__(self, args):
        """Constructor and Attributes"""

        self._proxy = args.proxy
        self._random_proxy = args.random_proxy

    def run(self) -> dict:
        """Performs the Proxy selection operation"""

        if self._proxy is not None:
            return self.format_proxy()

        if self._random_proxy:
            return Proxy.random_proxy()

    @staticmethod
    def random_proxy() -> dict:
        """Consumes an API that returns from random proxies returning a JSON"""

        # Checks the status of the proxy
        while True:
            random_proxy = get(
                "https://www.proxyscan.io/api/proxy?format=json&type=https&level=anonymous,elite&ping=100").json()
            if random_proxy[0]['Location']['status'] == "success":
                break

        # Configures the proxy PORT and IP.
        port_proxy = random_proxy[0]["Port"]
        ip_proxy = random_proxy[0]["Ip"] + ":" + str(port_proxy)

        # Checks the proxy protocol.
        while True:
            try:
                protocol_proxy = random_proxy[0]['Type'][1]
                break
            except IndexError:
                protocol_proxy = random_proxy[0]['Type'][0]
                break
        protocol_proxy = protocol_proxy.lower() + "://"

        return {protocol_proxy: ip_proxy}

    def format_proxy(self) -> dict:
        """ Formats the selected proxy accordingly. """

        if self._proxy[:7] == "http://":
            self._proxy = {'http://': self._proxy}
            Color.println("{+} Proxy: %s" % self._proxy['http://'])

        elif self._proxy[:8] == "https://":
            self._proxy = {'https://': self._proxy}
            Color.println("{+} Proxy: %s" % self._proxy['https://'])

        elif self._proxy[:3] == "ftp":
            self._proxy = {'ftp': self._proxy}
            Color.println("{+} Proxy: %s" % self._proxy['ftp'])

        else:
            self._proxy = {'': ''}

        return self._proxy
