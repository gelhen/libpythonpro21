# libpythonpro21
Módulo para exemplificar contrução de projetos Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto

Link do curso [Python Pro](https://pythonpro.com.br/)

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
