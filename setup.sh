#!/bin/bash

python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install flask

touch run.py
touch config.py

mkdir blogger
mkdir blogger/templates
mkdir blogger/static

mkdir instance
touch instance/config.py

pip freeze > requirements.txt

touch blogger/__init__.py
touch blogger/routes.py
touch blogger/models.py

deactivate
