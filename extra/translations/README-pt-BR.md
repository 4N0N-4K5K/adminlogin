# ⚡️ Heimdall ⚡️ [![English](https://img.shields.io/badge/en--US-English-blue.svg?style=flat-square&logo=Google%20Translate)](https://github.com/ygorsimoes/Heimdall/blob/master/README.md)

![Build](https://github.com/ygorsimoes/Heimdall/workflows/build/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat&logo=)](https://github.com/ygorsimoes/Heimdall/blob/master/LICENSE) 
[![Python3.9](https://img.shields.io/badge/Python-3.9-yellow.svg?style=flat&logo=python)](https://www.python.org/) 
[![Releases](https://img.shields.io/github/v/release/ygorsimoes/Heimdall?include_prereleases)](https://github.com/ygorsimoes/Heimdall/releases/tag/v5.3.3.9-stable)
[![Last Commit](https://img.shields.io/github/last-commit/ygorsimoes/Heimdall?color=blue&style=flat-square-circle)](https://github.com/ygorsimoes/Heimdall/commits/main)

Heimdall é uma ferramenta de código aberto projetada para automatizar a busca no painel de administração de um site de destino usando força bruta na lista de palavras. Desenvolvido inteiramente em Python, possui código didático simples para estudo, e é uma ferramenta ideal para arsenal de hacking.

![Heimdall2Gif](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/extra/images/heimdall2.gif)

## ⚡️ Requerido

É extremamente importante que você tenha as ferramentas obrigatórias listadas abaixo para que o Heimdall funcione conforme o esperado.
É recomendável que você use um sistema operacional com foco no Pentest.

* [`python`](https://www.python.org/): "Only version 3 of python is supported."
* [`requests`](https://requests.readthedocs.io/) "A simple, yet elegant HTTP library."

## ⚡️ Capturas de tela

![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/extra/images/screenshots/5.1-stable/screenshot02.png)

Você pode visitar a coleção de capturas de tela que demonstram o funcionamento em algumas plataformas clicando [aqui](https://github.com/ygorsimoes/Heimdall/tree/master/doc/images/screenshots).

## ⚡️ Instalação

Você pode baixar o tarball mais recente clicando em [aqui](https://github.com/ygorsimoes/Heimdall/tarball/master) ou o zipball mais recente clicando em [aqui](https://github.com/ygorsimoes/Heimdall/zipball/master).

Baixe o projeto:
```zsh
$ git clone https://github.com/ygorsimoes/Heimdall.git
```

Entre na pasta do projeto e instale:
```zsh
$ cd Heimdall && pip3 install -r requirements.txt
```

Execute o Heimdall:
```zsh
$ python3 heimdall.py
```

Qualquer dúvida, erro ou solução, entre em contato com um dos desenvolvedores do projeto.

## ⚡️ Modo de uso

![Screenshot](https://raw.githubusercontent.com/ygorsimoes/Heimdall/master/extra/images/screenshots/5.1-stable/screenshot01.png)

### ⚡️ Exemplos

```zsh
./heimdall.py --url www.site_target.com --wordlist 1
./heimdall.py --url www.site_target.com --wordlist 2 --user-agent <USER-AGENT>
./heimdall.py --url www.site_target.com --wordlist extra/wordlists/custom.txt
./heimdall.py --update
```

## ⚡️ Licence

`Heimdall` é feito com ♥ por [YGÃO](https://github.com/ygorsimoes) e é lançado sob a licença do MIT.

[![Ygor Simões](https://img.shields.io/badge/perfil-Ygor%20Sim%C3%B5es%20(YG%C3%83O)-red.svg?style=for-the-badge&logo=github)](https://github.com/ygorsimoes/)