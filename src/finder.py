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

from requests import get

from src.config import Config
from src.core.color import Color

date_now = datetime.now().strftime("%m-%d-%Y - %H-%M-%S")


class Finder:
    def __init__(self, args):
        """
        Constructor and Attributes
        """
        self._url = args.url
        self._wordlist = args.wordlist
        self._proxy = args.proxy
        self._user_agent = args.user_agent

    def dashboard(self):
        """
        Heimdall, find!
        """
        Color.println("{+} User-Agent: %s" % self._user_agent['User-Agent'])

        """
        Format the target URL as simple.
        Select the output directory.
        """
        url_simple = Config.target_simple(self._url)
        path_out = os.path.realpath(f"output/{url_simple}/{date_now}/")

        """
        Create the output directory.
        """
        os.makedirs(path_out)
        Color.println("{+} Output: '%s'" % path_out)

        """
        Creates the "info.txt" file to 
        write the attack specifications.
        """
        output_info = open(os.path.realpath(f"{path_out}/info.txt"), 'w')
        output_info.writelines(f"[+] URL (Target): {self._url}\n"
                               f"[+] Proxy: {self._proxy}\n"
                               f"[+] User-Agent: {self._user_agent}\n"
                               f"[+] Output: {path_out}\n\n"
                               f"[+] Wordlist: {self._wordlist}")
        output_info.close()

        """
        Starts the request loop to the target.
        """
        Color.println("\n{+} {G}Heimdall, find the dashboard!{W}\n")
        for link in self._wordlist:
            target = self._url + link.rstrip("\n")
            request = get(target, proxies=self._proxy, headers=self._user_agent)
            if request.status_code == 200:
                """
                Create the file "sites-found.txt" to
                write the possible directories found.
                """
                output_sites_found = open(os.path.realpath(f"{path_out}/sites-found.txt"), 'a')
                output_sites_found.writelines("\n" + target)
                output_sites_found.close()
                Color.println("{+} {G}%s{W}" % target)
            else:
                """
                Creates the file "sites-not-found.txt" to
                write the directories not found.
                """
                output_sites_not_found = open(os.path.realpath(f"{path_out}/sites-not-found.txt"), 'a')
                output_sites_not_found.write("\n" + target)
                output_sites_not_found.close()
                Color.println("{-} %s" % target)
