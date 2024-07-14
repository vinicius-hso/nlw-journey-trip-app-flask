# shebang
#!/bin/bash

# criando diretórios
mkdir .vscode init src src/main src/main/controllers src/main/routes src/main/server src/models src/models/repositories src/models/settings

# criando __init__.py
touch .vscode/settings.json storage.db run.py .gitignore init/schema.sql src/__init__.py src/main/controllers/__init__.py src/main/__init__.py src/main/server/__init__.py src/main/routes/__init__.py src/models/__init__.py src/models/repositories/__init__.py src/models/settings/__init__.py

# virtual env
# python3 -m venv venv
