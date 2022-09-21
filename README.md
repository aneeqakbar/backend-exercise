# backend-exercise
For job interview

### How to run

1: `pip install -r requirements.txt`

2: `python manage.py makemigrations && python manage.py migrate && python manage.py runserver`

3: Start redis server using this command: `redis-server`

4: Run celery in a seperate terminal: `celery -A core worker -l INFO`