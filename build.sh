pip install -r requirements.txt
python -m gensim.downloader --download glove-wiki-gigaword-50
python manage.py collectstatic --noinput
python manage.py migrate
