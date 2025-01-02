FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir build setuptools && pip install --no-cache-dir .


# Alkalmazás futtatása
CMD ["python", "app.py"]
