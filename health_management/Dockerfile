FROM bitnami/python:3.12.0
WORKDIR /health_management

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
