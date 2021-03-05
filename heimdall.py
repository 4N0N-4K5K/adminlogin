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

import argparse

from src.core.config import Config
from src.core.color import Color
from src.core.strings import Strings
from src.core.update import Update

from src.finder import Finder
from src.utils.check import Check
from src.utils.setter import Setter

"""
Try to import libraries.
"""
try:
    from requests import get
except ModuleNotFoundError as ex:
    Color.println("{!} %s Please install requirements: {R}pip3 install -r requirements.txt{W}" % ex)

"""
Capture all passed 
command line arguments.
"""
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-h", "--help",
                    action="store_true",
                    help="Show this help message and exit")

parser.add_argument("-u", "--url",
                    action="store",
                    type=str,
                    default=False,
                    help="Target URL (http://www.site_target.com/)")

parser.add_argument("-w", "--wordlist",
                    action="store",
                    type=str,
                    default="1",
                    help="Set wordlist. Default: 1 (Small) and Max: 3 (Big)")

parser.add_argument("-p", "--proxy",
                    action="store",
                    type=str,
                    default=None,
                    help="Use a proxy to connect to the target URL")

parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=None,
                    help="Customize the User-Agent. Default: Random User-Agent")

parser.add_argument("--update",
                    action="store_true",
                    default=False,
                    help="Upgrade Heimdall to its latest available version")

parser.add_argument("--no-update",
                    action="store_true",
                    default=False,
                    help="Disables the intention of updates")

parser.add_argument("--no-logo",
                    action="store_true",
                    default=False,
                    help="Disable the initial banner")

if __name__ == '__main__':
    """
    Stores all command line arguments 
    passed in the variable.
    """
    args = parser.parse_args()

    """
    Get the Heimdall settings, updates and 
    pass it on to the Strings class.
    """
    String = Strings()

    """
    Print the banner along with 
    Heimdall specifications.
    """
    if not args.no_logo:
        String.banner()
        String.banner_description()

    """
    Check for available updates.
    """
    conf = Config()
    update = Update()

    if args.update and update.verify(args.update):
        update.upgrade()

    if conf.get_automatic_verify_upgrades and not args.update:
        update.verify(args.update)

    """
    Activates the "helper()" method if no 
    targets are passed in the arguments.
    """
    if not args.url:
        String.helper()
        exit()
    else:
        """
        Format the target URL accordingly.
        """
        args.url = Config.target(args.url)

        """
        Instance the "Request" class.
        Generates a random User-Agent.
        """
        Set = Setter(args)
        args.user_agent = Set.user_agent()

        """
        Formats the selected proxy.
        """
        if args.proxy is not None:
            args.proxy = Set.proxy()

        """
        Instance the "Check" class.
        Checks whether the target is online.
        """
        Checkup = Check(args)
        try:
            Checkup.target()
            Color.println("{+} Target On: {G}%s{W}" % args.url)
        except Exception as ex:
            Color.println("{!} Error: %s" % ex)
            Color.println("{!} Please verify your target.")
            exit()

        """
        Stores the selected word list in the variable.
        """
        args.wordlist = Set.wordlist()

        """
        Instance the "Finder" class.
        Heimdall, find!
        """
        ExploitFinder = Finder(args)
        try:
            ExploitFinder.dashboard()
        except KeyboardInterrupt as ex:
            Color.println("\n{!} CTRL + C has pressed. %s" % ex)
    Color.println("{+} Finished!    :)")
