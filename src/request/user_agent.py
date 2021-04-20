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
from random import choice


class UserAgent:
    def __init__(self, args):
        self._user_agent = args.user_agent

    def run(self) -> dict:
        """
        Method that reads text files containing thousands of User-Agents
        using the "random" library to generate just one random User-Agent.
        """

        if self._user_agent is not None:
            return {'User-Agent': self._user_agent}

        # Returns the random User-Agent.
        return {'User-Agent': self.random_user_agent()}

    def random_user_agent(self) -> str:
        """Load all files with User-Agents and return a list."""

        user_agent_chrome_text = open(os.path.realpath("extra/user-agents/Chrome.txt"), 'r')
        chrome = user_agent_chrome_text.readlines()
        user_agent_chrome_text.close()

        user_agent_edge_text = open(os.path.realpath("extra/user-agents/Edge.txt"), 'r')
        edge = user_agent_edge_text.readlines()
        user_agent_edge_text.close()

        user_agent_firefox_text = open(os.path.realpath("extra/user-agents/Firefox.txt"), 'r')
        firefox = user_agent_firefox_text.readlines()
        user_agent_firefox_text.close()

        user_agent_opera_text = open(os.path.realpath("extra/user-agents/Opera.txt"), 'r')
        opera = user_agent_opera_text.readlines()
        user_agent_opera_text.close()

        user_agent_safari_text = open(os.path.realpath("extra/user-agents/Safari.txt"), 'r')
        safari = user_agent_safari_text.readlines()
        user_agent_safari_text.close()

        user_agents = chrome + edge + firefox + opera + safari
        self._user_agent = choice(user_agents).rstrip('\n')

        return self._user_agent
