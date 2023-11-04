FROM python:3.8-slim

WORKDIR /app
COPY ./app /app/
RUN pip install --no-cache-dir -r requirements.txt --progress-bar off
EXPOSE 80
CMD ["python", "app.py"]
