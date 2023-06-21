#! /bin/bash

echo "[ Reset test data ]"

echo "Move project root folder"
SCRIPT_FILE_PATH="$(dirname -- "${BASH_SOURCE[0]}")"
cd $SCRIPT_FILE_PATH
cd ..
pwd

echo "Remove DB"
rm db.sqlite3

echo "Remove media files"
rm -rf media/uploads

echo "Makemigrations"
poetry run python manage.py makemigrations

echo "Migrate"
poetry run python manage.py migrate

echo "Run test data generator"
poetry run python manage.py runscript scripts.test_data_generator

echo "Finished."