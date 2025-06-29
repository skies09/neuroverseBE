# 1. build.sh (make it executable with chmod +x build.sh)
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# 2. requirements.txt (update your existing one)
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
python-decouple==3.8
Pillow==10.0.1
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.7
dj-database-url==2.1.0
