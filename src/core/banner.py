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

from src.core.config import Config
from src.core.color import Color


class Strings(Config):

    def __init__(self):
        """
        Constructor and Attributes
        """
        super().__init__()

    @staticmethod
    def helper():
        print("""
Usage: python3 heimdall.py --help

Description: Heimdall is an open source tool designed to automate fetching 
             from a target site's admin panel using brute force in the wordlist.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://testphp.vulnweb.com/)
   -t, --threads          Set threads number. Default: 8
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   -p, --proxy            Use a proxy to connect to the target URL
   --random-proxy         Use a random anonymous proxy
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --no-redirects         Option to disregard redirects to avoid false positives.
   --update               Upgrade Heimdall to its latest available version.
   
   --no-update            Disables the intention of updates
   --no-logo              Disable the initial banner\n""")

    @staticmethod
    def banner():
        """Print the pure colored Heimdall banner."""

        Color.println(r"""{O}________________________________________________________________
                    _               _       _ _ 
          /\  /\___(_)_ __ ___   __| | __ _| | |
         / /_/ / _ \ | '_ ` _ \ / _` |/ _` | | |
        / __  /  __/ | | | | | | (_| | (_| | | |
        \/ /_/ \___|_|_| |_| |_|\__,_|\__,_|_|_|{W}""")

    def banner_description(self):
        """Print design and author specifications."""

        print(f"""\n                      Version: {self.get_version}
    Author: {self.get_author} (Security Researcher)
        GitHub: {self.get_github}""")
        Color.println("{O}________________________________________________________________{W}\n")


if __name__ == '__main__':
    String = Strings()
    String.banner()
    String.banner_description()
