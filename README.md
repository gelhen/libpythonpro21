# libpythonpro21
Módulo para exemplificar contrução de projetos Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto

Link do curso [Python Pro](https://pythonpro.com.br/)

[![Build Status](https://app.travis-ci.com/gelhen/libpythonpro21.svg?branch=main)](https://app.travis-ci.com/gelhen/libpythonpro21)
[![Updates](https://pyup.io/repos/github/gelhen/libpythonpro21/shield.svg)](https://pyup.io/repos/github/gelhen/libpythonpro21/)
[![Python 3](https://pyup.io/repos/github/gelhen/libpythonpro21/python-3-shield.svg)](https://pyup.io/repos/github/gelhen/libpythonpro21/)

Suportada a versão 3 de Python

Para instalar:

```console
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Para conferir qualidade do código:

```console
flake8 
```

Tópicos a serem abordados:
 1. Git
 2. Virtualenv
 3. Pip

Criar .gitignore_global
```text
No diretório home do usuário, criar o arquivo .gitignore_global, contendo:
Pycharm files
.idea/
.classpath
.project
.settings/
bin/
*.sqlite3

```
Para informar ao git que ignore os arquivos globalmente

```shell
git config --global core.excludesFile ~/.gitignore_global
```
