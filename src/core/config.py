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

import json
import os
import pathlib


class Config:
    """
    Constructor and Attributes
    """

    def __init__(self):

        # Load archive config.json
        path_dir = pathlib.Path("src/core/config.json")
        with open(path_dir) as file_config_json:
            self.__config_json = json.load(file_config_json)

        # Specifications
        self.__authors = self.__config_json["specifications"]["author"]
        self.__version = self.__config_json["specifications"]["version"]
        self.__github = self.__config_json["specifications"]["github"]
        self.__email = self.__config_json["specifications"]["email"]

        # Update and Upgrade
        self.__api_repository = self.__config_json["update"]["api_repository"]
        self.__automatic_upgrades = bool(self.__config_json["update"]["automatic_upgrades"])

    @staticmethod
    def target(url):
        """
        Format the target URL accordingly.
        """
        if url[:7] != "http://" and url[:8] != "https://":
            url = "http://" + url
        if url[-1] != "/":
            url = url + "/"
        return url

    @staticmethod
    def target_simple(url):
        """
        Format the target URL as simple.
        """
        if url[:7] == "http://":
            url = url.replace("http://", "")
        elif url[:8] == "https://":
            url = url.replace("https://", "")
        if url[-1] == "/":
            url = url.replace("/", "")
        return url

    # Getters
    @property
    def get_author(self):
        return self.__authors

    @property
    def get_version(self):
        return self.__version

    @property
    def get_github(self):
        return self.__github

    @property
    def get_email(self):
        return self.__email

    @property
    def os(self):
        return self.os

    # Update and Upgrade
    @property
    def get_repository(self) -> str:
        return self.__api_repository

    @property
    def get_automatic_upgrades(self) -> bool:
        return self.__automatic_upgrades


# if __name__ == "__main__":
#     Config()
