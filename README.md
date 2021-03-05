# ⚡️ Heimdall ⚡️

![Build](https://github.com/ygorsimoes/Heimdall/workflows/build/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/ygorsimoes/Heimdall/blob/master/LICENSE) 
[![Python3.9](https://img.shields.io/badge/Python-3.9-yellow.svg?style=flat&logo=python)](https://www.python.org/) 
[![Releases](https://img.shields.io/badge/release-v5.0--stable-green)](https://github.com/ygorsimoes/Heimdall/releases/tag/v5.0-stable)


Heimdall is an open source tool designed to automate fetching from a target site's admin panel using brute force in the wordlist. Developed entirely in Python, it has simple didactic code for study, and is an ideal tool for hacking arsenal.

![Heimdall2Gif](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/heimdall2.gif)

## Required

It is extremely important that you have the mandatory tools listed below for Heimdall to work as expected.
It is recommended that you use an operating system with a focus on Pentest.

* [`python`](https://www.python.org/): (Only version 3 of python is supported.)
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## Installation

You can download the latest tarball by clicking [here](https://github.com/ygorsimoes/Heimdall/tarball/master) or latest zipball by clicking [here](https://github.com/ygorsimoes/Heimdall/zipball/master).

    $ git clone https://github.com/ygorsimoes/Heimdall.git
    $ cd Heimdall && pip3 install -r requirements.txt

## Usage

```
Usage: python3 heimdall.py [-h, --help] [-u, --url] [-w, --wordlist (1, 2, 3)]
                           [-p, --proxy <proxy>][--user-agent <custom>] [--update]

Description: Heimdall is an open source tool designed to automate fetching 
             from a target site's admin panel using brute force in the wordlist.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site_target.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   -p, --proxy            Use a proxy to connect to the target URL
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --update               Upgrade Heimdall to its latest available version.
   
   --no-update            Disables the intention of updates
   --no-logo              Disable the initial banner
```

## Screenshots

![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/screenshots/5.1--stable/screenshot01.png)
![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/screenshots/5.1--stable/screenshot02.png)

You can visit the collection of screenshots that demonstrate how it works on some platforms by clicking [here](https://github.com/ygorsimoes/Heimdall/tree/master/doc/images/screenshots).

### Examples

```
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Translations

* [English](https://github.com/ygorsimoes/Heimdall/blob/master/README.md)
* [Portuguese](https://github.com/ygorsimoes/Heimdall/blob/master/doc/translations/README-pt-BR.md)

# Author
* [Ygor Simões (@ygorsimoes)](https://github.com/ygorsimoes/)
