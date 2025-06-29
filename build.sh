# 1. build.sh (make it executable with chmod +x build.sh)
#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔍 Current working directory: $(pwd)"
echo "📄 Contents of requirements.txt:"
cat requirements.txt

pip install -r requirements.txt

pip freeze  # Confirm packages installed

python manage.py collectstatic --no-input
python manage.py migrate
