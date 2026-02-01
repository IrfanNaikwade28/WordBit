#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# ⬇️ Download GloVe model at build time (IMPORTANT)
python -m gensim.downloader --download glove-wiki-gigaword-50

python manage.py collectstatic --noinput
python manage.py migrate
