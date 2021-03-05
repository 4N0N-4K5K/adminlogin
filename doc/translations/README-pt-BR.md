# ⚡️ Heimdall ⚡️

![Build](https://github.com/ygorsimoes/Heimdall/workflows/build/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/ygorsimoes/Heimdall/blob/master/LICENSE) 
[![Python3.9](https://img.shields.io/badge/Python-3.9-yellow.svg?style=flat&logo=python)](https://www.python.org/) 
[![Releases](https://img.shields.io/badge/release-v5.1--stable-green)](https://github.com/ygorsimoes/Heimdall/releases/tag/v5.1-stable)

Heimdall é uma ferramenta de código aberto projetada para automatizar a busca no painel de administração de um site de destino usando força bruta na lista de palavras. Desenvolvido inteiramente em Python, possui código didático simples para estudo, e é uma ferramenta ideal para arsenal de hacking.

![Heimdall2Gif](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/heimdall2.gif)

## Requerido

É extremamente importante que você tenha as ferramentas obrigatórias listadas abaixo para que o Heimdall funcione conforme o esperado.
É recomendável que você use um sistema operacional com foco no Pentest.

* [`python`](https://www.python.org/): (Only version 3 of python is supported.)
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## Capturas de tela

![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/screenshots/5.1-stable/screenshot01.png)
![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/doc/images/screenshots/5.1-stable/screenshot02.png)

Você pode visitar a coleção de capturas de tela que demonstram o funcionamento em algumas plataformas clicando [aqui](https://github.com/ygorsimoes/Heimdall/tree/master/doc/images/screenshots).

## Instalação

Você pode baixar o tarball mais recente clicando em [aqui](https://github.com/ygorsimoes/Heimdall/tarball/master) ou o zipball mais recente clicando em [aqui](https://github.com/ygorsimoes/Heimdall/zipball/master).

    $ git clone https://github.com/ygorsimoes/Heimdall.git
    $ cd Heimdall && pip3 install -r requirements.txt

## Modo de uso

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

### Exemplos

```
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## Traduções

[![Inglês](https://img.shields.io/badge/en--US-Inglês-blue.svg?style=flat-square&logo=Google%20Translate)](https://github.com/ygorsimoes/Heimdall#%EF%B8%8F-heimdall-%EF%B8%8F)
[![Português](https://img.shields.io/badge/pt--BR-Português-blue.svg?style=flat-square&logo=Google%20Translate)](https://github.com/ygorsimoes/Heimdall/blob/master/doc/translations/README-pt-BR.md)

## Autor:

[![Ygor Simões](https://img.shields.io/badge/Perfil-Ygor%20Sim%C3%B5es%20(YG%C3%83O)-red.svg?style=for-the-badge&logo=github)](https://github.com/ygorsimoes/)