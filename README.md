# ⚡️ Heimdall ⚡️ [![Portuguese](https://img.shields.io/badge/pt--BR-Portuguese-blue.svg?style=flat-square&logo=Google%20Translate)](https://github.com/ygorsimoes/Heimdall/blob/master/doc/translations/README-pt-BR.md)

![Build](https://github.com/ygorsimoes/Heimdall/workflows/build/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/ygorsimoes/Heimdall/blob/master/LICENSE) 
[![Python3.9](https://img.shields.io/badge/Python-3.9-yellow.svg?style=flat&logo=python)](https://www.python.org/) 
[![Releases](https://img.shields.io/badge/release-v5.2.3.9-beta--stable-green)](https://github.com/ygorsimoes/Heimdall/releases/tag/v5.2.3.9-beta)
[![Last Commit](https://img.shields.io/github/last-commit/ygorsimoes/Heimdall?color=blue&style=flat-square-circle)](https://github.com/ygorsimoes/Heimdall/commits/main)

Heimdall is an open source tool designed to automate fetching from a target site's admin panel using brute force in the wordlist. Developed entirely in Python, it has simple didactic code for study, and is an ideal tool for hacking arsenal.

![Heimdall2Gif](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/extra/images/heimdall2.gif)

## ⚡️ Required

It is extremely important that you have the mandatory tools listed below for Heimdall to work as expected.
It is recommended that you use an operating system with a focus on Pentest.

* [`python`](https://www.python.org/): (Only version 3 of python is supported.)
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## Screenshots

![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/extra/images/screenshots/5.1-stable/screenshot02.png)

You can visit the collection of screenshots that demonstrate how it works on some platforms by clicking [here](https://github.com/ygorsimoes/Heimdall/tree/master/doc/images/screenshots).

## ⚡️ Installation

You can download the latest tarball by clicking [here](https://github.com/ygorsimoes/Heimdall/tarball/master) or latest zipball by clicking [here](https://github.com/ygorsimoes/Heimdall/zipball/master).
Any questions, errors or solutions, contact one of the project's developers.

Download the project:
```zsh
$ git clone https://github.com/ygorsimoes/Heimdall.git
```

Enter the project folder and install:
```zsh
$ cd Heimdall && pip3 install -r requirements.txt
```

Run:
```zsh
$ python3 heimdall.py
```

## ⚡️ Usage

```
Usage: python3 heimdall.py --help

Description: Heimdall is an open source tool designed to automate fetching
             from a target site's admin panel using brute force in the wordlist.

Optional Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://testphp.vulnweb.com/)
   --wordlist (1, 2, 3)   Set wordlist. Default: 1 (Small) and Max: 3 (Big)
   -p, --proxy            Use a proxy to connect to the target URL
   --random-proxy         Use a random anonymous proxy
   --user-agent           Customize the User-Agent. Default: Random User-Agent
   --update               Upgrade Heimdall to its latest available version.

   --no-update            Disables the intention of updates
   --no-logo              Disable the initial banner
```

### ⚡️ Examples

```zsh
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## ⚡️ Licence

`Heimdall` is made with ♥ by [YGÃO](https://github.com/ygorsimoes) and it's released under the MIT license.


[![Ygor Simões](https://img.shields.io/badge/profile-Ygor%20Sim%C3%B5es%20(YG%C3%83O)-red.svg?style=for-the-badge&logo=github)](https://github.com/ygorsimoes/)