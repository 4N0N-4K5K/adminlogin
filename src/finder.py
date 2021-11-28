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

import os
from datetime import datetime
from threading import Thread

from requests import get

from src.core.config import Config
from src.core.color import Color

date_now = datetime.now().strftime("%m-%d-%Y - %H-%M-%S")


class Finder:

    def __init__(self, args):
        """Constructor and Attributes"""

        self.scanned = []
        self._url = args.url
        self.threads = args.threads
        self._wordlist = args.wordlist
        self._proxy = args.proxy
        self._user_agent = args.user_agent
        self._no_redirects = args.no_redirects
        self.path_out = ""

    def dashboard(self) -> None:
        """Heimdall, Dashboard!"""

        Color.println("{+} Follow redirects: %s" % self._no_redirects)
        Color.println("{+} User-Agent: %s" % self._user_agent['User-Agent'])

        # Format the target URL as simple and select the output directory.
        url_simple = Config.target_simple(self._url)
        self.path_out = os.path.realpath(f"output/{url_simple}/{date_now}/")

        # Create the output directory.
        os.makedirs(self.path_out)
        Color.println("{+} Output: '%s'" % self.path_out)

        # Creates the "info.txt" file to write the attack specifications.
        output_info = open(os.path.realpath(f"{self.path_out}/info.txt"), 'w')
        output_info.writelines(f"[+] URL (Target): {self._url}\n"
                               f"[+] Proxy: {self._proxy}\n"
                               f"[+] User-Agent: {self._user_agent}\n"
                               f"[+] Allow-Redirects: {self._no_redirects}\n"
                               f"[+] Output: {self.path_out}\n\n"
                               f"[+] Wordlist: {self._wordlist}")
        output_info.close()

    def find(self):
        """Heimdall, Find! """

        # Starts the request loop to the target.
        for link in self._wordlist:

            target = self._url + link.rstrip("\n")

            if target not in self.scanned:

                self.scanned.append(target)

                request = get(target, proxies=self._proxy, headers=self._user_agent)
                if self._no_redirects is False:
                    request = get(target, proxies=self._proxy, headers=self._user_agent, allow_redirects=self._no_redirects)

                if request.status_code == 200:
                    # Create the file "sites-found.txt" to write the possible directories found.
                    output_sites_found = open(os.path.realpath(f"{self.path_out}/sites-found.txt"), 'a')
                    output_sites_found.writelines("\n" + target)
                    output_sites_found.close()
                    Color.println("{+} {G}%s{W}" % target)

                else:
                    # Creates the file "sites-not-found.txt" to write the directories not found.
                    output_sites_not_found = open(os.path.realpath(f"{self.path_out}/sites-not-found.txt"), 'a')
                    output_sites_not_found.write("\n" + target)
                    output_sites_not_found.close()
                    Color.println("{-} %s" % target)

    def run(self):
        try:
            for j in range(self.threads):
                th = Thread(target=self.find)
                th.start()

        except (KeyboardInterrupt, SystemExit) as ex:
            Color.println("\n{!} CTRL + C has pressed. %s" % ex)
